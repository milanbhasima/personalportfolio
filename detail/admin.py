from django.contrib import admin
from .models import Contact,  BlogPost, Category, Tag
# Register your models here.
admin.site.register(Contact)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "status",
        "created_at",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_filter = (
        "status",
        "category",
    )

    search_fields = (
        "title",
        "content",
    )


admin.site.register(Category)
admin.site.register(Tag)