"""Example of dependency injection in Python."""

import flask
import logging

import containers as containers


def configure(binder):
    binder.bind(
        logging.Logger,
        to=containers.Core.logger(),
        scope=flask.request,
    )
