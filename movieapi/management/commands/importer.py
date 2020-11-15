import requests
from movieapi.models import Movie
from django.core.management.base import BaseCommand

IMPORT_URL = 'https://yts.mx/api/v2/list_movies.json'


class Command(BaseCommand):
    def import_movie(self, data):
        for data_object in data['data']['movies']:
            url = data_object.get('url', None)
            title = data_object.get('title', None)
            title_english = data_object.get('title_english', None)
            title_long = data_object.get('title_long', None)
            slug = data_object.get('slug', None)
            year = data_object.get('year', None)
            rating = data_object.get('rating', None)
            runtime = data_object.get('runtime', None)
            genres = data_object.get('genres', None)

            try:
                movie, created = Movie.objects.get_or_create(
                    url=url,
                    title=title,
                    title_english=title_english,
                    title_long=title_long,
                    slug=slug,
                    year=year,
                    rating=rating,
                    runtime=runtime,
                    genres=genres
                )
                if created:
                    movie.save()
                    display_format = "\nMovie, {}, has been saved."
                    print(display_format.format(movie))


            except Exception as ex:
                print("\n\nSomething went wrong saving this movie: {}\n{}".format(title, str(ex)))
                print("\n\nSomething went wrong saving this movie: {}\n{}".format(url, str(ex)))



    def handle(self, *args, **options):
        headers = {'Content-Type': 'application/json'}
        response = requests.get(
            url=IMPORT_URL,
            headers=headers,
        )

        response.raise_for_status()
        data = response.json()
        self.import_movie(data)













