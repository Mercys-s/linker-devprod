from django.contrib import admin

from .models import SubjectCategory , SubjectItem



class CategoryAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class SubjectAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    

admin.site.register (SubjectCategory , CategoryAdmin)
admin.site.register (SubjectItem , SubjectAdmin)