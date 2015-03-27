 # For each request, our application will be able to do the following:
 # 1) Read a cookie to figure out whether the current belongs to an existing session
 # 2) If a cookie is found, read an authentication from it and load the corresponding
 # session (if present) from the session store backend
 # 3) Loads some cached user information from the session. 

 config = {
 	'webapp2_extras.auth': {
 		'user_model': 'models.User',
 		'user_attributes': ['name']
 	},
 	'webapp2_extras.sessions': {
 		'secret_key': 'YOUR_SECRET_KEY'
 	}
 }