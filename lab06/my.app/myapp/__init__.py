from myapp.interfaces import INotification
from myapp.services import Basic, Twitter

from pyramid.config import Configurator



def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    
    config.registry.registerUtility(Basic(settings), INotification, 'basic')
    config.registry.registerUtility(Twitter(settings), INotification, 'twitter')

    #config.registry.registerUtility(MailService(settings), INotification, 'mail')

    #config.registry.registerUtility(Facebook(settings), INotification, 'facebook')

    #config.registry.registerUtility(Twitter(settings), INotification, 'twitter')


    config.scan()
    return config.make_wsgi_app()
