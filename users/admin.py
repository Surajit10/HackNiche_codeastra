from django.contrib import admin

# Register your models here.
from users.models import Contact,RegisterHackathon,Register,ParticipateHackathon

admin.site.register(Contact)
admin.site.register(RegisterHackathon)
admin.site.register(Register)
admin.site.register(ParticipateHackathon)