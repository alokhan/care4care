from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from main.models import User, VerifiedInformation

class CareUserAdmin(admin.ModelAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    #list_display = ('username', 'email', 'first_name', 'last_name', 'birth_date', 'is_staff')
    #list_filter = ('is_staff', 'is_superuser')
    #fieldsets = (
    #    (None, {'fields': ('email', 'password')}),
    #    ('Personal info', {'fields': ('first_name', 'last_name', 'credit', 
    #    	'birth_date', 'phone_number', 'mobile_number', 'location', 'latitude', 'longitude')}),
    #    ('Permissions', {'fields': ('is_verified', 'is_staff', 'is_superuser')}),
    #)
    ## add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    ## overrides get_fieldsets to use this attribute when creating a user.
    #add_fieldsets = (
    #    (None, {
    #        'classes': ('wide',),
    #        'fields': ('email', 'first_name', 'last_name', 'birth_date', 'password1', 'password2')}
    #    ),
    #)
    #search_fields = ('email',)
    #ordering = ('email',)
    #filter_horizontal = ()
    pass

admin.site.register(User, CareUserAdmin)


class VerifiedInformationAdmin(admin.ModelAdmin):
    pass

admin.site.register(VerifiedInformation, VerifiedInformationAdmin)