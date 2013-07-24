from pyramid.view import view_config

from ichnaea.db import Measure


def configure_content(config):
    config.add_route('homepage', '/')
    config.add_route('map', '/map')
    config.add_route('stats', '/stats')


@view_config(route_name='homepage', renderer='templates/homepage.pt')
def homepage_view(request):
    return {}


@view_config(route_name='map', renderer='templates/map.pt')
def map_view(request):
    return {}


@view_config(route_name='stats', renderer='templates/stats.pt')
def stats_view(request):
    session = request.database.session()
    result = {}
    result['total_measures'] = session.query(Measure).count()
    return result