from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized
from evento.models import *
from django.contrib.auth.models import *


class TipoInscricaoResource(ModelResource):
    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get']

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class EventoResource(ModelResource):
    class Meta:
        queryset = Evento.objects.all()
        allowed_methods = ['get']

class EventoCientificoResource(ModelResource):
    class Meta:
        queryset = EventoCientifico.objects.all()
        allowed_methods = ['get']

class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        allowed_methods = ['get']

class AutorResource(ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        allowed_methods = ['get']

class ArtigoCientificoResource(ModelResource):
    class Meta:
        queryset = ArtigoCientifico.objects.all()
        allowed_methods = ['get']

class InscricoesResource(ModelResource):
    class Meta:
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get']

class ArtigoAutorResource(ModelResource):
    class Meta:
        queryset = ArtigoAutor.objects.all()
        allowed_methods = ['get']