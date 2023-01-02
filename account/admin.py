from django.contrib import admin
from account.models import Account, MyAccountManage


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('id', 'email')
    search_fields = ('id',)
    list_filter = ('id',)


admin.site.register(Account, TodoAdmin)


