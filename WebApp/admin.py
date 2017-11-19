from django.contrib import admin
from WebApp.models import *
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(openBudgets)
admin.site.register(openBudgets.castInPlace)
admin.site.register(openBudgets.footings)
admin.site.register(openBudgets.slabOnGrade)
admin.site.register(openBudgets.tiltUp)
admin.site.register(mixDesign)
admin.site.register(openBudgets.slabOnDeck)
