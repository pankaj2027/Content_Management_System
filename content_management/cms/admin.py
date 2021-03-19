from django.contrib import admin
from .models import User,UserProfile


# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    class Meta:
        list_display = '__all__'
    inlines = (UserProfileInline, )