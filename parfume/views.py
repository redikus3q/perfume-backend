from parfume.serializers import ParfumeSerializer, ParfumeListSerializer, CommentSerializer, CommentListSerializer
from .models import Parfume, Comment
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User

import json


@csrf_exempt
def handle_parfumes(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        price = data['price']
        imageLink = data['imageLink']
        description = data['description']
        parfume = Parfume.objects.create(name=name,
                                       price=price,
                                       imageLink=imageLink,
                                       description=description)
        parfumeSerializer = ParfumeSerializer(parfume)
        jsonParfume = parfumeSerializer.data
        return JsonResponse(jsonParfume)

    if request.method == 'GET':
        parfumes = Parfume.objects.all()
        parfumesSerializer = ParfumeListSerializer(parfumes)
        jsonParfumes = parfumesSerializer.data
        return JsonResponse(jsonParfumes, safe=False)


@csrf_exempt
@permission_classes([IsAuthenticated])
def handle_parfume(request, id):
    if request.method == 'DELETE':
        parfume = get_object_or_404(Parfume, pk=id)
        parfume.delete()
        return JsonResponse({'success': True})

    if request.method == 'GET':
        parfume = get_object_or_404(Parfume, pk=id)
        parfumeSerializer = ParfumeSerializer(parfume)
        jsonParfume = parfumeSerializer.data
        return JsonResponse(jsonParfume)


@csrf_exempt
def handle_comments(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        parfumeId = data['flavorId']
        text = data['text']
        parfume = get_object_or_404(Parfume, pk=parfumeId)

        userToken = request.headers['Authorization']
        userTokenObj = AccessToken(userToken)
        userId = userTokenObj['user_id']
        user = get_object_or_404(User, pk=userId)

        comment = Comment.objects.create(parfume=parfume, text=text, user=user)
        commentSerializer = CommentSerializer(comment)
        jsonComment = commentSerializer.data
        return JsonResponse(jsonComment)


@csrf_exempt
def handle_parfume_comments(request, id):
    if request.method == 'GET':
        parfume = get_object_or_404(Parfume, pk=id)
        comments = Comment.objects.filter(parfume = parfume)
        commentSerializer = CommentListSerializer(comments)
        jsonComments = commentSerializer.data
        return JsonResponse(jsonComments, safe=False)


@csrf_exempt
def handle_comment(request, id):
    if request.method == "DELETE":
        comment = get_object_or_404(Comment, pk=id)
        comment.delete()
        return JsonResponse({'success': True})