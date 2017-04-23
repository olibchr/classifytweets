__author__ = 'oliver'

###START-CONF
##{
##"object_name": "inject",
##"object_poi": "my-inject-1234",
##"auto-load": false,
##"parameters": [ ],
##"return": [
##              {
##                      "name": "tweets",
##                      "description": "parsed tweets",
##                      "required": true,
##                      "type": "String",
##                      "state" : "UNCLASSIFIED"
##                  }
##
##          ] }
##END-CONF


from pumpkin import *
import twitter, sys, json
filter = sys.argv[1]

api = twitter.Api(consumer_key="Cwyqtxw3q9EaTwNmOo4nV5Rt3",
                  consumer_secret="iGNjEAsnpFC9Q9W0FAj19oI7ZTiaMELJ4DMTyBSmbmL2sMqUbC",
                  access_token_key="1207416314-EQvQPE8HspkhgRZj2DEkvwAycn1ChBCmlVbv6Gn",
                  access_token_secret="tC3L8c2ieXMqkI3a7hp2CTExbqjYrENGLoLa9H0Yn0DeT")

class inject(PmkSeed.Seed):

    def __init__(self, context, poi=None):
        PmkSeed.Seed.__init__(self, context,poi)
        pass


    def run(self, pkt):
        """ Data should be sourced here an injected into the
        data transformation network. In this example we are
        inject a single data "world" to a greeter which will
        tell us "hello"
        """
        results = api.GetSearch(term=filter, result_type="recent", count=100)
        self.dispatch(pkt, json.dumps({'tweets':results}), "UNCLASSIFIED")

        pass