from django.contrib import admin
from .models import Board, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt', 'tag_list')
    list_filter = ('modify_dt', )
    search_fields = ('title', 'content')
    inlines = [PhotoInline, ]
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())

