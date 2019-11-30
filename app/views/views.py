"""Applications views"""

import flask.views as flask_views


class RootView(flask_views.MethodView):

    def get(self):
        return "Hello World from RootView!"
