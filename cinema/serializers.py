from rest_framework import serializers
from cinema.models import Movie, Genre, Actor, MovieSession, CinemaHall


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name']


class ActorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name']

    def to_representation(self, instance):
        return f"{instance.first_name} {instance.last_name}"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class GenreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

    def to_representation(self, instance):
        return instance.name


class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreNameSerializer(many=True, read_only=True)
    actors = ActorNameSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'genres', 'actors']

class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'genres', 'actors']


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ['id', 'name', 'rows', 'seats_in_row', 'capacity']


class MovieSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title')
    cinema_hall_name = serializers.CharField(source='cinema_hall.name')
    cinema_hall_capacity = serializers.IntegerField(source='cinema_hall.capacity')

    class Meta:
        model = MovieSession
        fields = ['id', 'show_time', 'movie_title', 'cinema_hall_name', 'cinema_hall_capacity']


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = ['id', 'show_time', 'movie', 'cinema_hall']
