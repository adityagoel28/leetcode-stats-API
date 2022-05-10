from django.contrib import admin
from api.models import leetcodeUsername

class leetcodeUsernameAdmin(admin.ModelAdmin):
    list_display = ('username', 'count')
    search_fields = ('username',)

# Register your models here.
admin.site.register(leetcodeUsername, leetcodeUsernameAdmin)