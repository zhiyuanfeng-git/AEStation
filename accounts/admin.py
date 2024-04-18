from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.user import UserModel
from .forms import UserModelCreationForm, UserModelChangeForm
from django.utils.translation import gettext_lazy as _
# Register your models here.

class UserModelAdmin(UserAdmin):
    form = UserModelChangeForm
    add_form = UserModelCreationForm
    model = UserModel

    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

admin.site.register(UserModel, UserModelAdmin)
