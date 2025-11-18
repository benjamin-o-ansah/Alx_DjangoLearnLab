from django.contrib import admin
# from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title','author','publication_year')
#     search_fields = ("title", "author")
#     list_filter = ("publication_year",)

# admin.site.register(Book,BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ['username', 'email', 'is_staff', 'date_of_birth']

admin.site.register(CustomUser, CustomUserAdmin)