from django.contrib import admin

from .models import Report, TeamMember, Post, Project, Response, Shelter

admin.site.register(Report)
admin.site.register(Post)
admin.site.register(TeamMember)
admin.site.register(Project)
admin.site.register(Response)
admin.site.register(Shelter)
