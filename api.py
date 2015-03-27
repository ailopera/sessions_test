import webapp2
from webapp2_extras import sessions, sessions_memcache

class BaseHandler(webapp2.RequestHandler):
	def dispatch(self):
		# Get a session store for this request.
		self.session_store = sessions.get_store(request=self.request)

		try:
			# Dispatch the request.
			webapp2.RequestHandler.dispatch(self)
		finally:
			# Save all sessions.
			self.session_store.save_sessions(self.response)

	@webapp2.cached_property
	def session(self):
		# Returns a session using the default cookie key.
		return self.session_store.get_session(
			factory=sessions_memcache.MemcacheSessionFactory)


class HomeHandler(BaseHandler):
	def get(self):
		test_value = self.session.get('lomaranis')
		if test_value:
			self.response.write('Session has this value: %r.' % test_value)
		else:
			self.response.write('Session is empty.')

class LoginHandler(BaseHandler):
	def get(self):

		self.session['lomaranis'] = 'test'

	def post(self):
		session = self.session.get('lomaranis')
		self.response.write(session)



config = {}
config['webapp2_extras.sessions'] = {
	'secret_key': 'some-secret-key',
}

app = webapp2.WSGIApplication([
	('/Home', HomeHandler),
	('/Login', LoginHandler),
	], debug=True, config=config)
