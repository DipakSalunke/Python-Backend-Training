from django.contrib import admin
from .models import Developer,Skill
# Register your models here.

#admin.site.register(Developer)
#admin.site.register(Skill)
class SkillInLine(admin.StackedInline):
    model = Skill
    extra = 1

class DeveloperAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields':['name']}),
        ('Country', {'fields':['country'],}),
        ('Experience', {'fields':['experience']}),
    ]
    inlines = [SkillInLine]
    
admin.site.register(Developer, DeveloperAdmin)