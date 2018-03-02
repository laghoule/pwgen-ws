#!/usr/bin/env python3
# Pascal Gauthier <pgauthier@nihilisme.ca> <laghoule@gmail.com>
# 02.15.2018

from prometheus_client import start_http_server, Summary, Counter, Gauge
from flask import Flask, jsonify, request
from flasgger import Swagger
from flasgger.utils import swag_from
import random
import string

# Flask / swagger initialisation
app = Flask(__name__)
Swagger(app)

# Create metric with theses statistics
C_200 = Counter('pwgen_http_200_count', 'Number of http 200')
C_400 = Counter('pwgen_http_400_count', 'Number of http 400')
C_ALPHABET = Counter('pwgen_ptype_alphabet_count', 'Number password of type alphabet')
C_NUMERIC = Counter('pwgen_ptype_numeric_count', 'Number password of type numeric')
C_ALPHANUMERIC = Counter('pwgen_ptype_alphanumeric_count', 'Number password of type alphanumeric')
C_RANDOM = Counter('pwgen_ptype_random_count', 'Number password of type random')


@app.route('/api/<string:ptype>/', methods=['POST'])
@swag_from('swagger/api.yaml')
def pwgen(ptype: string) -> tuple:
    """
    Generate a password of size "size"

    :param ptype: Type of password to generate ("alphabet", "numeric", "alphanumeric", "random")
    :return: JSON of a generated password, or error
    """

    chars = None
    size = int(request.args.get('size', 1))

    if ptype.lower().strip() == "alphabet":
        C_ALPHABET.inc()
        chars = string.ascii_letters
    if ptype.lower().strip() == "alphanumeric":
        C_ALPHANUMERIC.inc()
        chars = string.ascii_letters + string.digits
    if ptype.lower().strip() == "numeric":
        C_NUMERIC.inc()
        chars = string.digits
    if ptype.lower().strip() == "random":
        C_RANDOM.inc()
        chars = string.ascii_letters + string.digits + string.punctuation

    if chars is None:
        C_400.inc()
        return jsonify(error="An error occurred, invalid password type", code="400"), 400

    if size > 512:
        C_400.inc()
        return jsonify(error="An error occurred, max size is 512", code="400"), 400

    password = ''.join(random.choice(chars) for _ in range(size))
    C_200.inc()

    return jsonify(password=password, type=ptype), 200


def main():
    """
    main funtion
    """

    # Start up the server to expose the metrics.
    start_http_server(5001)

    # Start the Flasgger application
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
