"""cripto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from web.views import index, fecha, Edad, plantilla
from django.conf import settings
from django.conf.urls.static import static
#en importar recordar importar el nombre de las vistas.
 
#la seccione de path es en verde la url que toca buscar y en blanco la vista que te abrira con esa url.
urlpatterns = [
    path('web/', include('web.urls')),
    path('admin/', admin.site.urls),
    path('index/', index),
    path("fecha/", fecha),
    path("futuro/<int:Edad_actual>/<int:ago>",Edad),
    path("plantilla/",plantilla),
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#Para poner una variable o dato en la url se pone <> y dentro el nombre de la variable.
#pero todo en los "" se toma como texto por eso se pasa a entero int:
    
]
