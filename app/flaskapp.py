"""Main entrypoint for application"""

import flask_injector

import views.views as views
import flask_inject_modules as fim


def run_app(app, host, port):
    """Run flask application

    :param app: app
    :param str host: hot
    :param int port: port
    """

    app.add_url_rule('/', view_func=views.RootView.as_view('root_view'))

    flask_injector.FlaskInjector(app=app, modules=[fim.configure])

    app.run(host=host, port=port)
