"""Run example application."""

import sys
import logging

import containers


if __name__ == '__main__':
    # Configure platform:
    containers.Core.config.override(
        {
            'database': {
                'dsn': ':memory:'
            },
            'aws': {
                'access_key_id': 'KEY',
                'secret_access_key': 'SECRET'
            },
            'flask_settings': {
                'host': '0.0.0.0',
                'port': 8080
            }
        }
    )

    console = logging.StreamHandler()
    console.setFormatter(
        logging.Formatter('%(name)s:: %(levelname)-1s [%(filename)s:%(lineno)d] %(message)s')
    )
    containers.Core.logger().addHandler(console)

    # Run application:
    containers.Application.main()
