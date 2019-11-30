"""Applications views"""

import flask.views as flask_views
import injector
import logging


class RootView(flask_views.MethodView):

    @injector.inject
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def get(self):
        self.logger.info('Hello from injected logger')
        return "Hello World from RootView!"
