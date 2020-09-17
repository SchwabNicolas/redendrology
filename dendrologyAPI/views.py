from django.shortcuts import render

from rest_framework import generics

from dendrologyAPI.models import Tree
from dendrologyAPI.serializers import TreeSerializer


class TreeCreate(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
