from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt
from .models import Inventario
import datetime, json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.

def index(request):
	return HttpResponse("En construcción...") 

# Vista para la pagina principal
def index(request):
	lista_inventarios = Inventario.objects.order_by('cantidad_sangre')


	context = {'lista_inventarios':lista_inventarios}

	return render(request, 'donaciones/index.html', context)

@xframe_options_exempt
@csrf_exempt
def inventarios(request):
	# La peticion debe ser en metodo GET
	if request.method == "GET":
			inventarios = Inventario.objects.all()
			data = []
			for inv in inventarios:
				data.append({
					'nombre': inv.banco.nombre,
					'categoria': inv.banco.categoria,
					'ciudad': inv.banco.ciudad.nombre,
					'localidad': inv.banco.localidad,
					'codigo_nacional_sangre': inv.banco.codigo_nacional_sangre,
					'ubicacion': 'https://www.google.com/maps/@' + str(inv.banco.lat) + ',' + str(inv.banco.lon) + ',15z',
					'direccion': inv.banco.direccion,
					'rh':inv.rh,
					'grupo_sanguineo':inv.grupo_sanguineo,
					'cantidad_sangre':inv.cantidad_sangre,
				})

			response = HttpResponse(json.dumps(data, cls=DjangoJSONEncoder))
			response['Access-Control-Allow-Origin'] = '*'
			return response
