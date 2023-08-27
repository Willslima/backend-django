from django.contrib import admin
from .models import Ceps, Endereco

# Register your models here.
admin.site.register(Ceps)
admin.site.register(Endereco)