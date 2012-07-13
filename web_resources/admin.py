from web_resources.models import Resource, Keyword, SubResource, Category
from django.contrib import admin



class KeywordInline(admin.TabularInline):
    model = Keyword
    extra = 1
    can_delete = False
    ordering = ('word',)

class SubResourceInline(admin.StackedInline):
    model = SubResource
    extra = 1
    can_delete = False
    ordering = ('title',)
    fk_name = 'parent'

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'href',)
    search_fields = ('title', 'id', 'href')

    fieldsets = [
        (None, {'fields': ['id', 'title', 'href']}),
    ]

    inlines = [KeywordInline, SubResourceInline]



admin.site.register(Resource, ResourceAdmin)

class KeywordAdmin(admin.ModelAdmin):
    list_display = ('word',)
    search_fields = ('word',)

admin.site.register(Keyword, KeywordAdmin)

class SubResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'href',)
    search_fields = ('title', 'id', 'href',)

admin.site.register(SubResource, SubResourceAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'id')
    search_fields = ('display_name', 'id')

admin.site.register(Category, CategoryAdmin)
