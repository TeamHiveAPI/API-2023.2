from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField, va
from wtforms.validators import DataRequired, Length

class CadastroForm(FlaskForm):
	nome = StringField(
		'Nome',
		validators=[DataRequired()]
	)

	dn = StringField(
		'DN',
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

	email = StringField(
		'Email',
		validators=[
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
		validators=[DataRequired()]
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

	senha = PasswordField(
		'Senha',
		[DataRequired()]
	)

	confirmar = PasswordField(
        'Confirm Your Password',
		[
            DataRequired(),
            EqualTo('senha', message='As senhas devem ser iguais.')
        ]
    )

	cadastrar = SubmitField('Cadastrar')

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

class LoginForm(FlaskForm):
	email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Digite um email válido.')
        ]
    )
    senha = PasswordField('Senha', validators=[DataRequired()])
    login = SubmitField('Log In')