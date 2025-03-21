from django.contrib import admin
from .models import Comment,Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','id','slug','author','publish','status','updated']
    list_filter = ['status','created','publish','author']
    search_fields = ['title','body']
    prepopulated_fields = {'slug':('title',)}
    #raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display =['name','email','body','post','created','updated','active']
    list_filter =['active','created','updated']
    search_fields =['name','email','body']

