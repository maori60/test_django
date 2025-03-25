from django.contrib import admin
from django.urls import path
from pages.views import home  # ⬅️ Import de ta vue

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # ⬅️ Ajout de la route d'accueil
]
