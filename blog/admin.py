from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    #no aparece porque solo hay uno user
    list_filter = ['status', 'created', 'publish', 'author']
    
    search_fields = ['title','body']
    
    date_hierarchy = 'publish'
    
    ordering = ['status', 'publish']
    
    prepopulated_fields = {'slug': ('title',)}
    
    raw_id_fields = ['author']
    
    show_facets = admin.ShowFacets.ALWAYS
    

#admin.site.register(Post)
