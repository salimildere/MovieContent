# Movie Content Service
It is a service where movie contents can be used with CRUD operations. This service can work together with the [Movie Catalog Service](https://github.com/salimildere/MovieCatalog) service.


### Run the app in Docker

Everything is containerized. So all you need is Docker installed, and then you can build and run:

```
docker-compose up -d --build
```

And your app will be up on the *port 8000*

### Test

```
docker exec -it log-movie_content_djangoContentService_1 python manage.py test
```

### Swagger OPENAPI Documentation

- http://localhost:8000/swagger/


### Django Admin Dashboard


You can create a super user to access admin Dashboard

```
docker exec -it log-movie_content_djangoContentService_1 python manage.py createsuperuser
```

Then you can be visit this url for admin page:

- http://localhost:8000/admin
