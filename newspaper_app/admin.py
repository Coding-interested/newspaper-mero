from django.contrib import admin

# Register your models here.


from newspaper_app.models import Post, Tag, Category, Contact, Comment

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Comment)