from django.contrib import admin

from movpro.contents.models import Genre, ContentRating, Person, Content

admin.site.register(Person)
admin.site.register(Genre)
admin.site.register(ContentRating)


# class CanNotCreateUpdateDelete(admin.ModelAdmin):
#     def has_add_permission(self, request, obj=None):
#         return False
#
#     def has_delete_permission(self, request, obj=None):
#         return False
#
#     def has_change_permission(self, request, obj=None):
#         return False
#
#
# @admin.register(Person)
# class PersonAdmin(CanNotCreateUpdateDelete):
#     pass
#
#
# @admin.register(Genre)
# class GenreAdmin(CanNotCreateUpdateDelete):
#     pass
#
#
# @admin.register(ContentRating)
# class ContentRatingAdmin(CanNotCreateUpdateDelete):
#     pass


@admin.register(Content)
class ContentsAdmin(admin.ModelAdmin):

    search_fields = (
        "title",
        "director__full_name",
    )
    list_display = (
        "id",
        "title",
        "made_year",
        "imdb_rating",
        "director",
    )
    list_editable = ("title",)
    list_filter = ("director",)
    list_per_page = 20

