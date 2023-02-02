from django.contrib import admin
from Tutor.models import User, Video, Category, Comment


class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Video, VideoAdmin)
admin.site.register(Comment)
# Register your models here.
