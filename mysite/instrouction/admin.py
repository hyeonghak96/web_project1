from django.contrib import admin

# Register your models here.

from instrouction.models import Instrouction


@admin.register(Instrouction)

class InstrouctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', ) #사이트출력목록
