#!/usr/bin/python
"""
basis of this code comes from:
http://bytes.com/topic/python/answers/19120-twisted-extending-portforward-simple-example
"""
from twisted.python import log
from twisted.protocols import portforward
from twisted.internet import reactor

import sys,re

class LoggingProxyClient(portforward.ProxyClient):

	def dataReceived(self, data):
		portforward.ProxyClient.dataReceived(self, data)

class LoggingProxyClientFactory(portforward.ProxyClientFactory):
	protocol = LoggingProxyClient

class LoggingProxyServer(portforward.ProxyServer):
	clientProtocolFactory = LoggingProxyClientFactory

	def __init__(self):
		self.seenUsernameToChange = 0

	def dataReceived(self, data):
		if self.seenUsernameToChange == 0:
			result = re.search("usernameToChange",data)
			if result:
				self.seenUsernameToChange = 1
				log.msg("first result matched. sRBL is: %i" % self.seenUsernameToChange)
				data = data.replace("usernameToChange","usernameToChangeTO")
			else:
				log.msg("first result no match")

		portforward.ProxyServer.dataReceived(self, data)

class LoggingProxyFactory(portforward.ProxyFactory):
	protocol = LoggingProxyServer

if __name__ == '__main__':

	log.startLogging(sys.stdout)

	fwd = LoggingProxyFactory('localhost', 25565)
	reactor.listenTCP(40321, fwd)
	reactor.run()
