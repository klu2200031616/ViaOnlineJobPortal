from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ViaUser)
admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(AppliedJobs)
admin.site.register(Contact)