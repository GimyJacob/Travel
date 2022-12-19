from django.contrib import admin
from .models import Place

admin.site.register(Place)
from .models import Person

admin.site.register(Person)

# Register your models here.
