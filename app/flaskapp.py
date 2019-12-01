"""Main entrypoint for application"""

import views.views as views


def root_view(logger):
    return '/', views.RootView.as_view(
            name='root_view',
            logger=logger
        )


def second_view(logger):
    return '/second', views.SecondView.as_view(
            name='second_view',
            logger=logger
        )


def run_app(app, host, port, app_views):
    """Run flask application

    :param app: app
    :param str host: hot
    :param int port: port
    :param list app_views: app views
    """

    for view in app_views:
        path, view_func = view()
        app.add_url_rule(path, view_func=view_func)

    app.run(host=host, port=port)
