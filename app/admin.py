from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from mapbox_location_field.admin import MapAdmin
from .models import Profile, Tree, Station, Ticket, Manufacture
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin




admin.site.site_header= "  پنل مدیریت  "
admin.site.site_title= "Tavankar"

admin.site.register(LogEntry)



#------------------------------------------------------------------------------
class TicketAdmin(ImportExportModelAdmin):
    list_display = ('user','to','title','created_on')
    list_filter = ("user", "to", "created_on")

admin.site.register(models.Ticket, TicketAdmin)



#------------------------------------------------------------------------------
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('user_name','phone','address')

admin.site.register(models.Profile, ProfileAdmin)



#------------------------------------------------------------------------------
class StationAdmin(ImportExportModelAdmin):
    list_display = ('name','manager','short_description','capacity','position')
    list_filter = ("manager", "position")

admin.site.register(models.Station, StationAdmin)



#------------------------------------------------------------------------------
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name','short_description','code','image_tag')

admin.site.register(models.Product, ProductAdmin)


#------------------------------------------------------------------------------
 #https://django-mptt.readthedocs.io/en/latest/admin.html#mptt-admin-draggablempttadmin
class TreeMPTTModelAdmin(ImportExportMixin, MPTTModelAdmin):
    mptt_level_indent = 15   # specify pixel amount for this ModelAdmin only
    #mptt_indent_field = "some_node_field"

admin.site.register(Tree, DraggableMPTTAdmin,
    list_display=('tree_actions','indented_title','position'),
    #list_editable = ('quantity'),
    list_display_links=('indented_title',),)



#------------------------------------------------------------------------------
class ManufactureAdmin(ImportExportModelAdmin):
    list_display = ('product','description')

admin.site.register(models.Manufacture, ManufactureAdmin)
