from django.contrib import admin

from portfolio.landingpage.models import AboutMe
from portfolio.landingpage.models import Projects
from portfolio.landingpage.models import Skills


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "image",
        "image_2",
        "url",
        "live_url",
    )
    list_filter = ("title",)
    search_fields = ("title",)


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "image",
    )
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
    )
    list_filter = ("title",)
    search_fields = ("title",)
