from helloworld.models import Funcionario, Setor
from django import forms

class InsereFuncionarioForm(forms.ModelForm):
	class Meta:
		model = Funcionario

		fields = [
			'nome',
			'cpf',
			'tempo_de_servico',
			'remuneracao'
		]	

class InsereSetorForm(forms.ModelForm):
	class Meta:
		model = Setor

		fields = [
			'nome',
			'responsavel',
			'num_sala'
		]