from django.contrib import admin

from .models import Task, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'due_date', 'created_by', 'is_completed')
    inlines = [
        CommentInline,
    ]

admin.site.register(Task, TaskAdmin)