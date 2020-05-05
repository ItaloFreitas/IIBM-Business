from django.urls import path
from website.views import IndexTemplateView, FuncionarioListView, SetorListView, FuncionarioUpdateView, SetorUpdateView, FuncionarioDeleteView, SetorDeleteView, FuncionarioCreateView, SetorCreateView

app_name = 'website'

urlpatterns = [

	path('', IndexTemplateView.as_view(), name='index'),
	
	path(
		'funcionarios/',
		FuncionarioListView.as_view(),
		name='lista_funcionarios'),

	path(
		'setores/',
		SetorListView.as_view(),
		name='lista_setores'),

	path(
		'funcionario/<pk>',
		FuncionarioUpdateView.as_view(),
		name='atualiza_funcionario'),

	path(
		'setor/<pk>',
		SetorUpdateView.as_view(),
		name='atualiza_setor'),

	path(
		'funcionario/excluiF/<pk>',
		FuncionarioDeleteView.as_view(),
		name='deleta_funcionario'),

	path(
		'setor/excluir/<pk>',
		SetorDeleteView.as_view(),
		name='deleta_setor'),

	path(
		'funcionario/cadastrar/',
		FuncionarioCreateView.as_view(),
		name='cadastra_funcionario'),

	path(
		'setor/cadastrar/',
		SetorCreateView.as_view(),
		name='cadastra_setor'),




]