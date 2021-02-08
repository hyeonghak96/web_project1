from django.contrib import admin
from assessment.models import Interface_project, Post
from assessment.models import Interface,edge_device, gateway_device, iot_project, mix_project

@admin.register(Post) #decorator
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('title','content')
    # prepopulated_fields = { 'slug' : ('title', )}

@admin.register(Interface) #decorator
class InterfaceAdmin(admin.ModelAdmin):
    list_display = ('user', 'performance', 'writing','attitude','Portfolio')
    search_fields = ('title','content')

@admin.register(Interface_project) #decorator
class Interface_projectAdmin(admin.ModelAdmin):
    list_display = ('user', 'performance', 'writing','attitude','Portfolio')
    search_fields = ('title','content')

@admin.register(edge_device) #decorator
class edge_deviceAdmin(admin.ModelAdmin):
    list_display = ('user', 'performance', 'writing','attitude','Portfolio')
    search_fields = ('title','content')

@admin.register(gateway_device) #decorator
class gateway_deviceAdmin(admin.ModelAdmin):
    list_display = ('user', 'performance', 'writing','attitude','Portfolio')
    search_fields = ('title','content')

@admin.register(iot_project) #decorator
class iot_projectAdmin(admin.ModelAdmin):
    list_display = ('user', 'performance', 'writing','attitude','Portfolio')
    search_fields = ('title','content')

@admin.register(mix_project) #decorator
class mix_projectAdmin(admin.ModelAdmin):
    list_display = ('user', 'performance', 'writing','attitude','Portfolio')
    search_fields = ('title','content')







