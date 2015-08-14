import logging
import tweepy

from myapp.interfaces import INotification

from zope.interface import implements

logger = logging.getLogger(__name__)

class Basic(object):

    implements(INotification)

    def __init__(self, settings):
        self.settings = settings

    def send(self, message):
        logger.debug("Sending a basic notification! --> " + message)



class Twitter:
    
    implements(INotification)

    def __init__(self, settings):
        self.settings = settings

    def send(self, message):
            
        auth = tweepy.OAuthHandler(self.settings['twitter.consumer_key'], self.settings['twitter.consumer_secret'])
        auth.set_access_token(self.settings['twitter.key'], self.settings['twitter.secret'])

        api = tweepy.API(auth)

        status = api.update_status(status = message)
        
        return status.id
