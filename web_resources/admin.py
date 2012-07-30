from web_resources.models import Resource, Keyword, PrimaryResource, Category
from django.contrib import admin



class KeywordInline(admin.TabularInline):
    model = Keyword
    extra = 1
    can_delete = False
    ordering = ('word',)

class ResourceInline(admin.StackedInline):
    model = PrimaryResource.subresources.through 
    fk_name = 'primaryresource'
    extra = 1
    can_delete = False

class PrimaryResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'url',)
    list_filter = ('primary_category',)
    search_fields = ('name', 'id', 'url')

    filter_horizontal = ('categories', 'subresources',)

    fieldsets = [
        (None, {'fields': ['id', 'name', 'url', 'primary_category', 'categories']}),
        ('Descriptions', {'fields': ['desc', 'shortdesc', 'longdesc']}),
        ('Sub-Resources', {'fields': ['subresources']})
    ]

    inlines = [KeywordInline]



admin.site.register(PrimaryResource, PrimaryResourceAdmin)

class KeywordAdmin(admin.ModelAdmin):
    list_display = ('word',)
    search_fields = ('word',)

admin.site.register(Keyword, KeywordAdmin)

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url',)
    search_fields = ('name', 'id', 'url',)

admin.site.register(Resource, ResourceAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'id')
    search_fields = ('display_name', 'id')

admin.site.register(Category, CategoryAdmin)
