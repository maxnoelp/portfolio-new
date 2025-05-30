from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from tinymce.models import HTMLField


class Skills(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    image = FilerImageField(
        verbose_name=_("Image"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="svg",
    )

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")

    def __str__(self):
        return self.name


class Projects(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    code = models.ManyToManyField(Skills, verbose_name=_("Code"))
    description = HTMLField(
        _("Description"),
    )
    image = FilerImageField(
        verbose_name=_("Image"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="image",
    )
    image_2 = FilerImageField(
        verbose_name=_("Image 2"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="image_2",
    )
    url = models.URLField(_("Github URL"), blank=True)
    live_url = models.URLField(_("Live URL"), blank=True)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    description = HTMLField(
        _("Description"),
    )

    def __str__(self):
        return self.title
