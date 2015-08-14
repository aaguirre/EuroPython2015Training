from myapp.events import NewNotification

from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'my.app'}

@view_config(name='testing',renderer='json')
def testing(request):
    request.registry.notify(
       NewNotification(request=request, message='hello bilbao!')
    )

    return {
       'sent':'ok'
    }
