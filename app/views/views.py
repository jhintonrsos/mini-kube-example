"""Applications views"""

import flask.views as flask_views


class RootView(flask_views.MethodView):

    def __init__(self, **kwargs):
        self.logger = kwargs.get('logger')

    def get(self):
        self.logger.info('Hello from injected logger')

        msg = """
        <p>Hello World from RootView!</p>
        <br>
        <a href="/second">Next Page</a>
        """

        return msg


class SecondView(flask_views.MethodView):

    def __init__(self, **kwargs):
        self.logger = kwargs.get('logger')

    def get(self):
        self.logger.info('Hello from injected logger')

        msg = """
        <p>Hello World from RootView!</p>
        <br>
        <a href="/">Previous Page</a>
        """

        return msg
