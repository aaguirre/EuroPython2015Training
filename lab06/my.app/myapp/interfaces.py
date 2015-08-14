from zope.interface import Interface

class INotification(Interface):
    """ Service responsible of sending notifications ."""

    def send(self, message): pass
