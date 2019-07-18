from django.db import models
from django.contrib.auth.models import User
from django import forms


class NovoLink(models.Model):
    titulo = models.CharField(max_length=255, null=False)
    url=models.CharField(max_length=255, null=False)
    data_criacao=models.CharField(max_length=255, null=False)
    usuario=models.ForeignKey(User, related_name="usuario")

    def esconder(self):
    	exibe=True;
    	pass   # adicionar código do toggle de exibe/esconde
   

class NovoForm(forms.Form):
	titulo=forms.CharField(required=True)
	url=forms.CharField(required=True) 

	#adicionar validações do formulário nessa classe

class RegistrarUsuario(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.CharField(required=True)
    senha = forms.CharField(required=True)
    telefone = forms.CharField(required=True)
    
    def is_valid(self):
        valid=True
        if not super(RegistrarUsuario, self).is_valid():
            self.adiciona_erro("Por favor, verifique os dados informados")
            valid=False

        user_exists = User.objects.filter(username=self.data["nome"]).exists()
        if user_exists:
            self.adiciona_erro("Usuario ja existente")
            valid=False

        return valid


    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)

class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone=models.CharField(max_length=15, null=False)
    usuario=models.OneToOneField(User, related_name="perfil")

    @property
    def email(self):
        return self.usuario.email
