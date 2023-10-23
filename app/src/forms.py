from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class CadastroForm(FlaskForm):
	nome = StringField(
		'Nome',
		[DataRequired()]
	)

	dn = StringField(
		'DN',
		[DataRequired()]
	)

	cpf = StringField(
		'CPF',
		[
			DataRequired(),
			Length(11)
		]
	)

	endereço = StringField(
		'Endereço',
		[DataRequired()]
	)

	email = StringField(
		'Email',
		[
			DataRequired(),
			Email(message='Digite um e-mail válido.')
		]
	)

	parentesco = SelectField(
		'Grau de parentesco',
		choices=[
			'Mãe/pai',
			'Avô/avó',
			'Irmão/irmã',
			'Tia/tio',
			'Outro'
		]
	)

	profissao = StringField(
		'Profissão',
		[DataRequired()]
	)

	comochegou = SelectField(
		'Como chegou ao site?'
		choices=[
			'Internet',
			'Redes sociais',
			'Indicação de amigo',
			'Indicação profissional',
			'Outro'
		]
	)

	senha = StringField(
		'Senha',
		[DataRequired()]
	)

class PostForm(FlaskForm):
	titulo = StringField(
		'Título',
		[DataRequired()]
	)

	conteudo = StringField(
		'Depoimento',
		[DataRequired()]
	)

	enviar = SubmitField('Enviar')