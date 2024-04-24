from django.urls import path
from . import views

urlpatterns = [
    path("retornar", views.retornar, name="retornar"),
    path("retornar2", views.retornar2, name="retornar2"),
    path("template2", views.template2, name="template2")
]