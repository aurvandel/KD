from django.contrib import admin
from WebApp.models import *
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(openBudgets)
admin.site.register(openBudgets.castInPlace)
admin.site.register(openBudgets.castInPlace.footings)
admin.site.register(openBudgets.castInPlace.footings.slabOnGrade)
admin.site.register(openBudgets.castInPlace.footings.slabOnGrade.tiltUp)
admin.site.register(mixDesign)
