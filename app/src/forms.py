from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, EmailField, PasswordField, DateField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class CadastroForm(FlaskForm):
	nome = StringField(
		'Nome completo',
		validators=[DataRequired()]
	)

	dn = DateField(
		'Data de nascimento',
		validators=[DataRequired()]
	)

	cpf = StringField(
		'CPF',
		validators=[
			DataRequired(),
			Length(11)
		]
	)

	endereco = StringField(
		'Endereço',
		validators=[DataRequired()]
	)

	email = EmailField(
		'Email',
		validators=[
			DataRequired(),
			Email(message='Digite um email válido.')
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
		validators=[DataRequired()]
	)

	comochegou = SelectField(
		'Como chegou ao site?',
		choices=[
			'Internet',
			'Redes sociais',
			'Indicação de amigo',
			'Indicação profissional',
			'Outro'
		]
	)

	senha = PasswordField(
		'Senha',
		validators=[DataRequired()]
	)

	confirmar = PasswordField(
		'Confirme sua senha',
		validators=[
			DataRequired(),
			EqualTo('senha', message='As senhas devem ser iguais.')
		]
	)

	submit = SubmitField('Cadastrar')

class PostForm(FlaskForm):
	titulo = StringField(
		'Título',
		[DataRequired()]
	)

	conteudo = TextAreaField(
		'Depoimento',
		[DataRequired()]
	)

	submit = SubmitField('Enviar')

class LoginForm(FlaskForm):
	email = StringField(
		'Email',
		validators=[
			DataRequired(),
			Email(message='Digite um email válido.')
		]
	)
	senha = PasswordField('Senha', validators=[DataRequired()])
	submit = SubmitField('Log In')