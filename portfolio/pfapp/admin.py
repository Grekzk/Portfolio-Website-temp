from django.contrib import admin
from .models import Project, Experience, Education, ProfessionalSkills, Languages


class ProjectAdmin(admin.ModelAdmin):
    pass


class ExperienceAdmin(admin.ModelAdmin):
    pass


class EducationAdmin(admin.ModelAdmin):
    pass


class ProfessionalSkillsAdmin(admin.ModelAdmin):
    pass


class LanguagesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(ProfessionalSkills, ProfessionalSkillsAdmin)
admin.site.register(Languages, LanguagesAdmin)
