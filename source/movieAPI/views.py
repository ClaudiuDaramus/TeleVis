# Create your views here.
# -*- coding: utf-8 -*-

from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from tvgrid.recommandationHelper import WeightedIntervalScheduling
from .movieManager import bigSearchForVideoContent, oldFormatResponseForInterest, searchForVideoContent, \
    calculateVideoInterestScoreUpgraded

from rest_framework import status
from .models import VideoContent
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .movieManager import bigSearchForVideoContent, oldFormatResponseForInterest, searchForVideoContent, \
    calculateVideoInterestScoreUpgraded
from tvgrid.scheduleHelper import formatResponseForInterest
from .serializers import VideoContentSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def searchForMovieView(request):
    title = request.GET.get('title')

    try:
        search = bigSearchForVideoContent(title)
        return JsonResponse({'results': search})
    except Exception as e:
        return JsonResponse({'error': str(e)})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def findMovieView(request):
    title = request.GET.get('title')
    imdbId = request.GET.get('imdbId')
    # there is an error here i think idk what to do
    # try:
    search = searchForVideoContent(imdbId, title)
    videoSerializer = VideoContentSerializer(data=search)
    if videoSerializer.is_valid():
        found = VideoContent.objects.filter(imdbID=search['imdbID']).first()
        if found is None:
               createdVideo = videoSerializer.create(search)
    return JsonResponse({'results': search})
    # except Exception as e:
    #     return JsonResponse({'error': str(e)})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def compareMoviesView(request):
    firstMovie = request.GET.get('firstTitle')
    firstMovieID = request.GET.get('firstImdbId')
    secondMovie = request.GET.get('secondTitle')
    secondMovieID = request.GET.get('secondImdbId')

    try:
        firstMovie = searchForVideoContent(imdbID=firstMovieID, title=firstMovie)
        secondMovie = searchForVideoContent(imdbID=secondMovieID, title=secondMovie)

        firstMovieFormatted = formatResponseForInterest(firstMovie)
        secondMovieFormatted = formatResponseForInterest(secondMovie)

        interest = calculateVideoInterestScoreUpgraded([firstMovieFormatted], [secondMovieFormatted])
        return JsonResponse({'results': interest})

    except Exception as e:
        return JsonResponse({'error': str(e)})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def compareMovieListView(request):
    firstMovieList = request.GET.get('firstList')
    firstMovieList = None if firstMovieList is None else firstMovieList.split(',')
    firstMovieIDList = request.GET.get('firstIdList')
    firstMovieIDList = None if firstMovieIDList is None else firstMovieIDList.split(',')
    secondMovieList = request.GET.get('secondList')
    secondMovieList = None if secondMovieList is None else secondMovieList.split(',')
    secondMovieIDList = request.GET.get('secondIdList')
    secondMovieIDList = None if secondMovieIDList is None else secondMovieIDList.split(',')

    try:
        if firstMovieList is not None:
            firstMovieList = [searchForVideoContent(title=movie) for movie in firstMovieList]
        else:
            firstMovieList = []

        if firstMovieIDList is not None:
            for movieID in firstMovieIDList:
                firstMovieList.append(searchForVideoContent(imdbID=movieID))

        if secondMovieList is not None:
            secondMovieList = [searchForVideoContent(title=movie) for movie in secondMovieList]
        else:
            secondMovieList = []

        if secondMovieIDList is not None:
            for movieID in secondMovieIDList:
                secondMovieList.append(searchForVideoContent(imdbID=movieID))

        # elem1 = [movie['Runtime'] for movie in firstMovieList]
        # elem2 = [movie['Runtime'] for movie in secondMovieList]
        # print(elem1)
        # print(elem2)

        firstMovieList = [formatResponseForInterest(movie) for movie in firstMovieList]
        secondMovieList = [formatResponseForInterest(movie) for movie in secondMovieList]
        print(firstMovieList, secondMovieList)
        interest = calculateVideoInterestScoreUpgraded(firstMovieList, secondMovieList)
        return JsonResponse({'results': interest})

    except Exception as e:
        return JsonResponse({'error': str(e)})


@api_view(["GET"])
@permission_classes([AllowAny])
def createContent(request):
    video = VideoContentSerializer.create("test", "test", "test", "test", "test")
    return video
