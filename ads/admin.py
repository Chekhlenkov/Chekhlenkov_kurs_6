from django.contrib import admin

from ads.models import Ad, Comment


class CommentAdAdmin(admin.StackedInline):

    model = Comment
    list_display = ('author',)
    readonly_fields = ('created_at', 'ad')
    extra = 0


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('author', 'ad')
    list_filter = ('author', )


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    list_display = ('author', 'title', 'price', 'created_at', 'image_', )
    list_filter = ('created_at', 'author')
    readonly_fields = ("image_", )
    search_fields = ('title', 'post_text')
    ordering = ['-created_at']
    list_per_page = 10
    list_max_show_all = 100
    inlines = [CommentAdAdmin, ]


