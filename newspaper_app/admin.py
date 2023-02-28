from django.contrib import admin

# Register your models here.


from newspaper_app.models import Post, Tag, Category, Contact, Comment
from django_summernote.admin import SummernoteModelAdmin

# admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Comment)

from django_summernote.admin import SummernoteModelAdmin


# Apply summernote to content field in Post model.

class PostAdmin(SummernoteModelAdmin):   # instead of ModelAdmin
    summernote_fields = ("content",)
    list_display = ("title", "category", "author", "created_at")
    date_hierarchy = "published_at"

admin.site.register(Post, PostAdmin)

