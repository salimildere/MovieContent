from __future__ import unicode_literals

from django.db import models

from django.utils.translation import gettext_lazy as _
from movpro.utils.models import StarterModel


class Genre(StarterModel):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = _("Genres")
        verbose_name_plural = _("Genre")


class ContentRating(StarterModel):
    """
    Content rating, which indicates the content's suitability for children, teens, or adults.
    """

    label = models.CharField(max_length=100)
    icon = models.ImageField(
        upload_to="content_ratings/",
        verbose_name=_("image"),
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = _("Content Rating")
        verbose_name_plural = _("Content Ratings")


class Person(StarterModel):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to="peoples/",
        verbose_name=_("image"),
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Persons")
        verbose_name_plural = _("Person")


class Content(StarterModel):
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    imdb_rating = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
    )
    made_year = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to="content/",
        verbose_name=_("image"),
        null=True,
        blank=True,
    )
    director = models.ForeignKey(
        Person, on_delete=models.DO_NOTHING, related_name="director"
    )
    actress = models.ManyToManyField(Person, blank=True, related_name="actress")

    genre = models.ManyToManyField(Genre, blank=True)
    content_rating = models.ForeignKey(ContentRating, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Contents")
        verbose_name_plural = _("Content")
