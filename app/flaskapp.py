import views.views as views


def run_app(app, host, port):
    """Run flask application

    :param app: app
    :param str host: hot
    :param int port: port
    """

    app.add_url_rule('/', view_func=views.RootView.as_view('root_view'))
    app.run(host=host, port=port)
