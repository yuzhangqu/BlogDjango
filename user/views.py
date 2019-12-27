from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
import json
from .models import User

# Create your views here.
def uid_view(request, uid):
    ids = range(1, uid)
    return render(request, 'uid.html', {'ids':ids})
    # return JsonResponse({'id':uid})

def reg(request):
    try:
        payload = json.loads(request.body)
        email = payload['email']
        qs = User.objects.filter(email=email)
        if qs:
            return HttpResponseBadRequest()
        
        name = payload['name']
        password = payload['password']
        
        user = User()
        user.name = name
        user.password = password
        user.email = email
        
        try:
            user.save()
        except Exception:
            raise

        return JsonResponse({"id":user.id})
    except Exception as e:
        print(e)
        return HttpResponseBadRequest()