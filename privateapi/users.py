from django.contrib.auth.models import User

def create(username,email,password):
	user = User.objects.create_user(username, email, password)
	user.is_staff = False
	user.save()
	return True
