from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Lecture)
class LectureAdmin(admin.ModelAdmin):

    """ Lecture Admin Definition """

    pass
