from django.http import HttpResponse
from django.http import JsonResponse

def prueba(request):
    #numbers = sorted(request.GET['numbers'].split(','))
    numbers2 = sorted(request.GET['numbers'].split(','))
    #json = {key: value for key,value in enumerate(numbers)}
    
    json2 = {
        'status':'ok',
        'numbers':numbers2,
        'message':'Integers sorted successfully'
    }
    #return JsonResponse(json)
    return JsonResponse(json2)