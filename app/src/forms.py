from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class FormCadastro(FlaskForm):
	nome = StringField(
		'Nome',
		validators=[DataRequired()]
	)

	dn = StringField(
		'DN',
		validators[DataRequired()]
	)

	cpf = StringField(
		'CPF',
		validators[
			DataRequired()
			Length(11)
		]
	)

	endereço = StringField(
		'Endereço',
		validators[DataRequired()]
	)

	email = StringField(
		'Email',
		validators[
			DataRequired()
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