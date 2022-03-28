import random
from decimal import Decimal

import factory


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'contents.Genre'

    label = factory.Faker("word")


class ContentRatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'contents.ContentRating'

    label = factory.Faker("word")


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'contents.Person'

    full_name = factory.Faker("word")


class ContentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'contents.Content'

    description = factory.Faker("sentence")
    title = factory.Faker("word")
    is_active = factory.Faker("boolean")
    imdb_rating = factory.LazyAttribute(lambda x: Decimal(random.randrange(1, 10)))
    made_year = factory.LazyAttribute(lambda x: Decimal(random.randrange(1950, 2022)))
    director = factory.SubFactory(PersonFactory)
    actors = factory.SubFactory(PersonFactory)
    genres = factory.SubFactory(GenreFactory)
    content_rating = factory.SubFactory(ContentRatingFactory)

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create or not extracted:
            self.genres.add(GenreFactory())
            return
        self.genres.add(*extracted)

    @factory.post_generation
    def actors(self, create, extracted, **kwargs):
        if not create or not extracted:
            self.actors.add(PersonFactory())
            return
        self.actors.add(*extracted)
