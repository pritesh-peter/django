from django.contrib import admin
from .models import Skill,Message

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')
    

class SkillAdmin(admin.ModelAdmin):
    list_display=('name','description')


admin.site.register(Skill,SkillAdmin)
admin.site.register(Message,MessageAdmin)
