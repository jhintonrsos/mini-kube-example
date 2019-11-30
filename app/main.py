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
    containers.Core.logger().addHandler(logging.StreamHandler(sys.stdout))

    # Run application:
    containers.Application.main()
