from django.urls import path
from clase.views import nuevo_curso
urlpatterns = [
    path('nuevo/', nuevo_curso, name='nuevo curso')
]
