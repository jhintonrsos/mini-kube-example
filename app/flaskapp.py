"""Main entrypoint for application"""

import collections as collections


FlaskView = collections.namedtuple('FlaskView', 'rule view_func')


def run_app(app, host, port, app_views):
    """Run flask application

    :param app: app
    :param str host: hot
    :param int port: port
    :param list app_views: app views
    """

    for view in app_views:
        url_rule = view()
        app.add_url_rule(url_rule.rule, view_func=url_rule.view_func)

    app.run(host=host, port=port)
