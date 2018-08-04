from django.db import models

# Create your models here.

class Departamento(models.Model):
	nombre = models.CharField(max_length=200)
	def __str__(self):
		return self.nombre

# Se crea la ciudad para poblar la base de datos
class Ciudade(models.Model):
	departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre + ' - ' + self.departamento.nombre
		
# Modelo proncipal, CIUDADANO
class Donante(models.Model):
	GRUPOS_SANGUINEOS = (
        ('Positivo', 'Positivo'),
        ('Negativo', 'Negativo'),
    )
	TIPOS_RH = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    )

	nombres = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	tipo_identificacion = models.ForeignKey(Identificacion, on_delete=models.CASCADE)
	identificacion = models.CharField(max_length=60, unique=True)
	fecha_nacimiento = models.DateField('Fecha Nacimiento')
	# References to ciudad
	ciudad_nacimiento = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='donante_ciudad_nacimiento')
	ciudad_domicilio = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='donante_ciudad_domicilio')
	rh = models.CharField(max_length=3, choices=TIPOS_RH)
	grupo_sanguineo = models.CharField(max_length=9, choices=GRUPOS_SANGUINEOS)
	estatura = models.FloatField(null=True)
	peso = models.FloatField(null=True)
	fecha_registro = models.DateTimeField(auto_now_add=True, editable=False)

	def __str__(self):
		return self.nombres + ' ' + self.apellidos


class Banco(models.Model):
	nombre = models.CharField(max_length=50,unique=True)
	categoria = models.CharField(max_length=2)
	ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='banco_ciudad')
	localidad = models.CharField(max_length=75)
	codigo_nacional_sangre = models.CharField(max_length=10,unique=True)
	lat = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)])
    lon = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)])
	direccion = models.CharField(max_length=50)
	"""docstring for Banco"""
	def __str__(self):
		return self.nombre



#class UnidadMovil(models.Model):
#	banco = models.ForeignKey(Banco, on_delete=models.CASCADE, related_name='unidad_banco')
#	nombre = models.CharField(max_length=50)
#	ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='unidad_ciudad')
#	codigo_nacional_sangre = models.CharField(max_length=10,unique=True)
#	lat = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)])
#    lon = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)])
#	direccion = models.CharField(max_length=50)
#	"""docstring for Banco"""
#	def __str__(self):
#		return self.nombre

