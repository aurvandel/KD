from django.contrib import admin
from WebApp.models import *
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(openBudgets)
admin.site.register(openBudgets.pendingBudgets.awardedBudgets.closedBudgets.castInPlace)
admin.site.register(openBudgets.pendingBudgets.awardedBudgets.closedBudgets.castInPlace.footings)
admin.site.register(openBudgets.pendingBudgets.awardedBudgets.closedBudgets.castInPlace.footings.slabOnGrade)
admin.site.register(openBudgets.pendingBudgets.awardedBudgets.closedBudgets.castInPlace.footings.slabOnGrade.tiltUp)
admin.site.register(openBudgets.pendingBudgets.awardedBudgets.closedBudgets.castInPlace.footings.slabOnGrade.tiltUp.mixDesign)
