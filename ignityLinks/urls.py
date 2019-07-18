from django.conf.urls import patterns, include, url
from ignityLinks import views
from ignityLinks.views import RegistrarNovoForm, RegistrarNovoUsuarioForm, index, perfillogado
from django.contrib.auth.models import User


urlpatterns = patterns('',
	url(r'^$', views.login, name="logar"),
	url(r'registrar', RegistrarNovoForm.as_view(), name="registrar"),
	url(r"^login/$", "django.contrib.auth.views.login", {"template_name":"login.html"}, name="login"),
	url(r"^novo-usuario/$", RegistrarNovoUsuarioForm.as_view(), name="novo-usuario"),
	url(r"^logout/$", "django.contrib.auth.views.logout_then_login", {"login_url":"/login/"}, name="logout"),
	url(r"^user/(?P<perfil_nome>\w+)$", views.exibirlinks, name="exibirlinks"),
	url(r"^id?", views.perfillogado, name="login"),
	url(r"^apaga/(?P<link_id>\d+)$", views.apagalink, name="apagalink"),

	
)
	