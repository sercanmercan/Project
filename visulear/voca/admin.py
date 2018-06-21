from django.contrib import admin
from . import models

admin.site.register(models.TestSet)
admin.site.register(models.Part)
admin.site.register(models.Question)
admin.site.register(models.UserAnswer)
