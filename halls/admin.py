from django.contrib import admin
from .models import Hall, Video


class HallAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user")
    list_display_links = ("title", "user")
    search_fields = ('title', )
    list_filter = ("user", )


class VideoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "hall")
    list_display_links = ("title", "hall")
    search_fields = ('title',)
    list_filter = ("hall", )


admin.site.register(Hall, HallAdmin)
admin.site.register(Video, VideoAdmin)
