"""Example of dependency injection in Python."""

import logging
import sqlite3

import boto3
import flask


import flaskapp as flaskapp
import services as services
import views.views as views

import dependency_injector.containers as containers
import dependency_injector.providers as providers


class Core(containers.DeclarativeContainer):
    """IoC container of core component providers."""

    config = providers.Configuration('config')

    logger = providers.Singleton(logging.Logger, name='example')


class Gateways(containers.DeclarativeContainer):
    """IoC container of gateway (API clients to remote services) providers."""

    database = providers.Singleton(sqlite3.connect, Core.config.database.dsn)

    s3 = providers.Singleton(
        boto3.client, 's3',
        aws_access_key_id=Core.config.aws.access_key_id,
        aws_secret_access_key=Core.config.aws.secret_access_key)


class Services(containers.DeclarativeContainer):
    """IoC container of business service providers."""

    photos = providers.Factory(
        services.PhotosService,
        db=Gateways.database,
        logger=Core.logger
    )


class FlaskApp(containers.DeclarativeContainer):
    """Container for flask"""

    app = providers.Singleton(
        flask.Flask,
        import_name='Sample flask app'
    )


class Application(containers.DeclarativeContainer):
    """IoC container of application component providers."""

    main = providers.Callable(
        flaskapp.run_app,
        app=FlaskApp.app,
        host=Core.config.flask_settings.host,
        port=Core.config.flask_settings.port
    )
