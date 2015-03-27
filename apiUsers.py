 # For each request, our application will be able to do the following:
 # 1) Read a cookie to figure out whether the current belongs to an existing session
 # 2) If a cookie is found, read an authentication from it and load the corresponding
 # session (if present) from the session store backend
 # 3) Loads some cached user information from the session. 

class BaseHandler(webapp2.RequestHandler):
	@webapp2.cached_property
	def auth(self):
		"""Shortcut to access the auth instance as a property."""
		return auth.get_auth()

	@webapp2.cached_property
	def user_info(self):
		""" Shortcut to access a subset of the user attributes that 
		are stored in the session.

		The list of attributes to store in the session is specified in 
		config['webapp2_extras.auth']['user_attributes'].

		:returns
			A dictionary with most user information
		"""
		return self.auth.get_user_by_session()

	@webapp2.cached_property
	def user(self):
		""" Shortcut to access the current logged in user.
		Unlike user_info, it fetches information from the persisence layers
		and returns an instance of the underlying model.
		:returns
			The instance of the user model associated to the logged in user.
		"""
		u = self.user_info
		return self.user_model.get_by_id(u['user_id']) if u else None


	@webapp2.cached_property
	def user_model(self):
		""" Shortcut to access the current session. 
			It is consistent with config ['webapp2_extras.auth']['user_model'], if set 
		"""
		return self.auth.store.user_model


	@webapp2.cached_property
	def session(self):
		"""Shortcut to access the current session."""
		return self.session_store.get_session(backend="datastore")


	def render_template(self, view_filename, params = {}):
		user = self.user_info
		params['user'] = user_info
		path = os.path.join(os.path.dirname(__file__), 'views', view_filename)
		self.response.out.write(template.render(path, params))

	def display_message(self, message):
		""" Utility function to display a template with a simple message. """
		params = {
			'message': message
		}
		self.render_template('message.html', params)

	# TODO
	def dispatch(self):
		pass





# TODO "Registration: Create new users"

 config = {
 	'webapp2_extras.auth': {
 		'user_model': 'models.User',
 		'user_attributes': ['name']
 	},
 	'webapp2_extras.sessions': {
 		'secret_key': 'YOUR_SECRET_KEY'
 	}
 }
