from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from app.models import Reviewer, Movie, MovieReview
from app.serializers import ReviewerSerializer, MovieSerializer, MovieReviewSerializer

def hello(request):
    return HttpResponse("Hello, welcome to the Movie Ratings application.")

class ReviewerListCreateAPIView(APIView):
    def get(self, request):
        all_reviewers = Reviewer.objects.all()
        serialized_reviewers = ReviewerSerializer(all_reviewers, many=True)
        return Response(serialized_reviewers.data, 200)

    def post(self, request):
        age = request.POST['age']
        occupation = request.POST['occupation']
        postal_code = request.POST['postal_code']
        new_reviewer = Reviewer.objects.create(age=age, occupation=occupation, postal_code=postal_code)
        serialized_reviewer = ReviewerSerializer(new_reviewer)
        return Response(serialized_reviewer.data, 201)

class ReviewerDetailAPIView(APIView):

    def get(self, request, pk):
        reviewer = Reviewer.objects.get(id=pk)
        serialized_reviewer = ReviewerSerializer(reviewer)
        return Response(serialized_reviewer.data, 200)

    def put(self, request, pk):
        reviewer = Reviewer.objects.get(id=pk)
        reviewer.age = request.POST['age']
        reviewer.occupation = request.POST['occupation']
        reviewer.postal_code = request.POST['postal_code']
        reviewer.save()
        serialized_reviewer = ReviewerSerializer(reviewer)
        return Response(serialized_reviewer.data, 200)

    def delete(self, response, pk):
        reviewer = Reviewer.objects.get(id=pk)
        reviewer.delete()
        return Response("", 204)

class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieReviewListCreateAPIView(APIView):

    def get(self, request):
        all_movie_reviews = MovieReview.objects.all()
        serialized_movie_reviews = MovieReviewSerializer(all_movie_reviews, many=True)
        return Response(serialized_movie_reviews.data, 200)

    def post(self, request):
        stars = request.POST['stars']
        notes = request.POST['notes']
        reviewer_id = request.POST.get('reviewer', None)
        movie_id = request.POST.get('movie', None)
        new_movie_review = MovieReview.objects.create(stars=stars, notes=notes, reviewer_id=reviewer_id, movie_id=movie_id)
        serialized_movie_review = MovieReviewSerializer(new_movie_review)
        return Response(serialized_movie_review.data, 201)

class MovieReviewDetailAPIView(APIView):
    def get(self, request, pk):
        movie_review = MovieReview.objects.get(id=pk)
        serialized_movie_review = MovieReviewSerializer(movie_review)
        return Response(serialized_movie_review.data, 200)

    def put(self, request, pk):
        movie_review = MovieReview.objects.get(id=pk)
        movie_review.stars = request.POST['stars']
        movie_review.notes = request.POST['notes']
        movie_review.reviewer_id = request.POST.get('reviewer', None)
        movie_review.movie_id = request.POST.get('movie', None)
        movie_review.save()
        serialized_movie_review = MovieReviewSerializer(movie_review)
        return Response(serialized_movie_review.data, 200)

    def delete(self, request, pk):
        movie_review = MovieReview.objects.get(id=pk)
        movie_review.delete()
        return Response("", 204)
