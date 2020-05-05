from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from helloworld.models import Funcionario, Setor
from website.forms import InsereFuncionarioForm, InsereSetorForm
from django.urls import reverse_lazy


# Create your views here.

#INDEX
class IndexTemplateView(TemplateView):
	template_name = "website/index.html"

#LISTAR
class FuncionarioListView(ListView):
	template_name = "website/listaF.html"
	model = Funcionario
	context_object_name = "funcionarios"

class SetorListView(ListView):
	template_name = "website/listaS.html"
	model = Setor
	context_object_name = "setores"

#ATUALIZAR (UPDATE)
class FuncionarioUpdateView(UpdateView):
	template_name = "website/atualizaF.html"
	model = Funcionario
	fields = '__all__'
	context_object_name = 'funcionario'
	success_url = reverse_lazy("website:lista_funcionarios")
	'''
	def get_object(self, queryset=None):
		funcionario = None
		id = self.kwargs.get(self.pk_url_kwargs)
		slug = self.kwargs.get(self.slug_url_kwargs)

		if id is not None:
			funcionario = Funcionario
			objects
			filter(id=id),
			first()
		elif slug is not None:
			campo_slug = self.get_slug_field()
			funcionario = Funcionario
			objects
			filter(**{campo_slug: slug})
			first()
		return funcionario
	'''

class SetorUpdateView(UpdateView):
	template_name = "website/atualizaS.html"
	model = Setor
	fields = '__all__'
	context_object_name = 'setor'
	success_url = reverse_lazy("website:lista_setores")
	'''
	def get_object(self, queryset=None):
		setor = None
		id = self.kwargs.get(self.pk_url_kwargs)
		slug = self.kwargs.get(self.slug_url_kwargs)

		if id is not None:
			setor = Setor
			objects
			filter(id=id)
			first()
		elif slug is not None:
			campo_slug = self.get_slug_field()
			setor = Setor
			objects
			filter(**{campo_slug: slug})
			first()
		return setor
	'''
class FuncionarioDeleteView(DeleteView):
	template_name = "website/excluiF.html"
	model = Funcionario
	context_object_name = 'funcionario'
	success_url = reverse_lazy(
		"website:lista_funcionarios"
	)

class SetorDeleteView(DeleteView):
	template_name = "website/excluiS.html"
	model = Setor
	context_object_name = 'setor'
	success_url = reverse_lazy(
		"website:lista_setores"
	)

class FuncionarioCreateView(CreateView):
	template_name = "website/criaF.html"
	model = Funcionario
	form_class = InsereFuncionarioForm
	success_url = reverse_lazy(
		"website:lista_funcionarios"
	)

class SetorCreateView(CreateView):
	template_name = "website/criaS.html"
	model = Setor
	form_class = InsereSetorForm
	success_url = reverse_lazy(
		"website:lista_setores"
	)
