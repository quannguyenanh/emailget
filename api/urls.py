from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import EmailGetHandler

class CsrfExemptResource( Resource ):
    def __init__( self, handler, authentication = None ):
        super( CsrfExemptResource, self ).__init__( handler, authentication )
        self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

emailget_resource = CsrfExemptResource( EmailGetHandler )

urlpatterns = patterns( '',
    url( r'^emailget/(?P<expression>.*)$', emailget_resource )
)
