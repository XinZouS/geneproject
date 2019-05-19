from django.views.generic import TemplateView

class HomePage(TemplateView):
	template_name = 'home.html'

class WelcomeLogin(TemplateView):
	template_name = 'welcome_login.html'

class WelgoLogout(TemplateView):
	template_name = 'welgo_logout.html'