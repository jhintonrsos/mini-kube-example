"""Example of dependency injection in Python."""

import flask
import logging
import injector

import containers as containers


class AppModule(injector.Module):
    """Application Module"""

    def __init__(self):
        super().__init__()

    def configure(self, binder):
        super().configure(binder)
        binder.bind(
            logging.Logger,
            to=containers.Core.logger(),
            scope=flask.request,
        )

# callable can be used in place of a Module
# def configure(binder):
#     binder.bind(
#         logging.Logger,
#         to=containers.Core.logger(),
#         scope=flask.request,
#     )
