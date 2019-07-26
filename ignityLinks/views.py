from django.shortcuts import render, redirect
from ignityLinks.models import NovoLink, NovoForm, RegistrarUsuario, Perfil
from django.views.generic import View
from django.contrib.auth.models import User
import datetime

def perfillogado(request):
    perfillog=get_perfil_logado(request)
    usuario= User.objects.get(username=perfillog.usuario.username)
    return render(request,"adicionalinks.html", {"novo_link": NovoLink.objects.filter(usuario=usuario), "perfis" : Perfil.objects.all(), "perfil_logado":get_perfil_logado(request)})

#def criaLinks(request):
 #   return render(request,"adicionalinks.html")

def index(request, perfil_id):
    return render(request,"adicionalinks.html", {"perfis" : Perfil.objects.all(), "perfil_logado":get_perfil_logado(request)})

def get_perfil_logado(request):
	return request.user.perfil

def login(request):
	return render(request,"login.html")	

def home(request):
    return render(request,"index.html")	

def precos(request):
    return render(request,"precos.html")	

def criaNovoLink(request):
    return render(request,"quasela.html")

class RegistrarNovoForm(View):

    template_name="adicionalinks.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
	    form = NovoForm(request.POST)
	    titulo=form.data["nomeUrl"]
	    url=form.data["linkUrl"]

	    perfillog=get_perfil_logado(request)
	    perfil=get_perfil_logado(request)
	    usuario= User.objects.get(username=perfillog.usuario.username)

	    novo_link = NovoLink(
				titulo=titulo, 
				url=url,
				data_criacao=datetime.datetime.now(),
				usuario=usuario,
				cliques=0
				)

	    novo_link.save()
	    return render(request,"adicionalinks.html", {"perfil" : perfil,"novo_link":NovoLink.objects.filter(usuario=usuario)})

class RegistrarNovoUsuarioForm(View):
	
	template_name="novo_registro.html"

	def get(self, request):
		return render(request, self.template_name)

	def post (self, request):
		form = RegistrarUsuario(request.POST)

		if form.is_valid():
			dados_form = form.data
			usuario= User.objects.create_user(dados_form["nome"],dados_form["email"], dados_form["senha"])

			perfil = Perfil(
				nome=dados_form["nome"], 
				email=dados_form["email"],
				telefone=dados_form["telefone"],
				usuario=usuario
				)

			perfil.save();

			return redirect("logar")

		return render(request, self.template_name, {"form": form})	


def exibirlinks(request, perfil_nome):
    
    perfil=Perfil.objects.get(nome=perfil_nome) # sintaxe pra buscar no banco de dados o perfil de perfil_id
    perfillog=get_perfil_logado(request)
    usuario= User.objects.get(username=perfillog.usuario.username)
    
    return render(request, "links.html", { "perfil" : perfil, "lista_links":NovoLink.objects.filter(usuario=usuario)})

def apagalink(request, link_id): #melhorar esse código, do jeito que está links estão expostos e podem ser facilmente apagados
    
    link_id=int(link_id) # converte string em número, para a query abaixo funcionar
    link=NovoLink.objects.get(id=link_id)
    link.delete()

    perfillog=get_perfil_logado(request)
    perfil=get_perfil_logado(request)
    usuario= User.objects.get(username=perfillog.usuario.username)
    
    return render(request,"adicionalinks.html", {"perfil" : perfil,"novo_link":NovoLink.objects.filter(usuario=usuario)})

def clicalink(request, link_id): #melhorar esse código, do jeito que está links estão expostos e podem ser facilmente apagados
    
    link_id=int(link_id) # converte string em número, para a query abaixo funcionar
    link=NovoLink.objects.get(id=link_id)
    link.incrementaClique()
    link.save()

    perfillog=get_perfil_logado(request)
    perfil=get_perfil_logado(request)
    usuario= User.objects.get(username=perfillog.usuario.username)

    return render(request, "links.html", { "perfil" : perfil, "lista_links":NovoLink.objects.filter(usuario=usuario)})

