from django.contrib import admin
from rental.models import Book, Rental

admin.site.register(Book)(admin.ModelAdmin)
admin.site.register(Rental)(admin.ModelAdmin)