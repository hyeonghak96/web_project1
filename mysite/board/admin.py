from django.contrib import admin
from board.models import Board, Album, Photo

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt', 'tag_list')
    list_filter = ('modify_dt', )
    search_fields = ('title', 'content')
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())

# @admin.register(Album)
# class AlbumAdmin(admin.ModelAdmin):
#     inlines = (PhotoInline,)
#     list_display = ('id', 'name', 'description')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')
# Register your models here.