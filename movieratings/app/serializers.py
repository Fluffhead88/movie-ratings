from rest_framework import serializers

from app.models import Reviewer, Movie, MovieReview

class ReviewerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviewer
        fields = ['id', 'age', 'occupation', 'postal_code']

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'imdb_link', 'director', 'release_year', 'genre']

class MovieReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieReview
        fields = ['id', 'reviewer', 'movie', 'stars', 'notes']
