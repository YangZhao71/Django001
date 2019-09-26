from django.views.generic import TemplateView

class HelloWorld(TemplateView):
	# HelloWorld is-a TemplateView
	template_name = 'test.html'
