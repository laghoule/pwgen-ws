#!/usr/bin/env python3
# Pascal Gauthier <pgauthier@nihilisme.ca> <laghoule@gmail.com>
# 02.15.2018

import connexion
import random
import string


def pwgen(size: int) -> dict:
    """
    Generate a password of size "size"
    :param size: Password size
    :return: JSON of a generated password
    """
    chars = string.ascii_uppercase + string.digits
    return {'password': ''.join(random.choice(chars) for _ in range(size))}


def main():
    """
    main funtion
    """

    app = connexion.FlaskApp(__name__, port=8090, specification_dir='swagger/')
    app.add_api('pwgen.yaml', arguments={'title': 'Password generator'})
    app.run()


if __name__ == '__main__':
    main()
