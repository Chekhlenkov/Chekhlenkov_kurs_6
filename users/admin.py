from django.contrib import admin
from users.models import User

@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('email', 'phone', 'role', 'image_',)
    readonly_fields = ("image_", "last_login")
    filter_horizontal = ()
    list_filter = ('role', 'email')
    list_per_page = 10
    list_max_show_all = 100
