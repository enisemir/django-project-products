from polls.models import Poll
from django.contrib import admin
from polls.models import Choice


# class PollAdmin(admin.ModelAdmin):
#     fields=['pub_date','question']
# admin.site.register(Poll,PollAdmin)

# class PollAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields':['question']}),
#         ('Date information', {'fields':['pub_date']}),
#     ]
# admin.site.register(Poll,PollAdmin)

class ChoiceInline (admin.TabularInline):
    model = Choice
    extra = 3
admin.site.register(Choice)

class PollAdmin (admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    search_fields = ['question']
    list_filter = ['pub_date']
    list_display = ('question', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
admin.site.register(Poll,PollAdmin)
