from myapp.async import greenlet
from myapp.events import NewNotification
from myapp.interfaces import INotification

from pyramid.events import subscriber


@subscriber(NewNotification)
def new_notification(event):   
    utilities = event.request.registry.getUtilitiesFor(INotification)
    
    @greenlet
    def send(utility, message):
        utility.send(message )
    
    for name, utility in utilities:
        send(utility, event.message)
         
