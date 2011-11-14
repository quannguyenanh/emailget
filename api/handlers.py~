from piston.handler import BaseHandler
import sys, re
class EmailGetHandler( BaseHandler ):
    def read( self, request, expression ):
        f = open(expression, 'r')
        out = open('/tmp/out.txt', 'w')
        out.write('\n'.join(re.findall('([\w\.\-]+@[\w\.\-]+)', f.read())))
