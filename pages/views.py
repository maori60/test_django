from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenue sur mon site Django déployé sur Render 🎉")
