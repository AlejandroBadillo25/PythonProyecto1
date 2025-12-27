from django.contrib import admin
from .models import Post
# Register your models here.

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "autor", "estado", "created_at"]
    list_filter = ["estado", "autor"]
    raw_id_fields = ["autor"]
    ordering = ["-created_at"]