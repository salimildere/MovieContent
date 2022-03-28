import random
from decimal import Decimal

import factory


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "contents.Genre"

    label = factory.Faker("word")


class ContentRatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "contents.ContentRating"

    label = factory.Faker("word")


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "contents.Person"

    full_name = factory.Faker("word")


class ContentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "contents.Content"

    description = factory.Faker("sentence")
    title = factory.Faker("word")
    is_active = factory.Faker("boolean")
    imdb_rating = factory.LazyAttribute(lambda x: Decimal(random.randrange(1, 10)))
    made_year = factory.LazyAttribute(lambda x: Decimal(random.randrange(1950, 2022)))
    director = factory.SubFactory(PersonFactory)
    actress = factory.SubFactory(PersonFactory)
    genre = factory.SubFactory(GenreFactory)
    content_rating = factory.SubFactory(ContentRatingFactory)

    @factory.post_generation
    def genre(self, create, extracted, **kwargs):
        if not create or not extracted:
            self.genre.add(GenreFactory())
            return
        self.genre.add(*extracted)

    @factory.post_generation
    def actress(self, create, extracted, **kwargs):
        if not create or not extracted:
            self.actress.add(PersonFactory())
            return
        self.actress.add(*extracted)
