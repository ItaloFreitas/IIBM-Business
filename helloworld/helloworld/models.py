from django.db import models

class Funcionario(models.Model):	
	nome = models.CharField(
		max_length = 255,
		null = False,
		blank = False
)

	cpf = models.CharField(
		max_length = 14,
		null = False,
		blank = False
)

	tempo_de_servico = models.IntegerField(
		default = 0,
		null = False,
		blank = False
)

	remuneracao = models.DecimalField(
		max_digits = 8,
		decimal_places = 2,
		null = False,
		blank = False
)

class Setor(models.Model):
	nome = models.CharField(
		max_length = 255,
		null = False,
		blank = False
)
	
	responsavel = models.CharField(
		max_length = 255,
		null = False,
		blank = False
)

	num_sala = models.CharField(
		max_length = 255,
		null = False,
		blank = False
)

objetos = models.Manager()
