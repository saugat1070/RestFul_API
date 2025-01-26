from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import PlatForm,WatchList
from .serializers import PlatFormSerializer,WatchListSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# particular_data = get,put,delete --> pk require
#list_data = get , post -->no pk require
from rest_framework.views import APIView

#for use mixins
from rest_framework import mixins
from rest_framework import generics

#for use endpoint on restframework
from rest_framework.reverse import reverse
from rest_framework.serializers import ValidationError 
from .models import Review
from .serializers import ReviewSerializer

@api_view(['GET'])
def api_root(request,format=None):
    return Response(
        {
            'movie':reverse('movie_list',request=request,format = format),
            'PlatForm':reverse('stream_list',request = request, format = format)
        }
    )



def home(request):
    return HttpResponse('<h1>hello world</h1>')


# @api_view(['GET'])
# def movie_list(request):
#     if request.method == 'GET':
#         list_name = WatchList.objects.all()
#         serializer_list = WatchListSerializer(list_name, many=True)
#         return Response(serializer_list.data)


# @api_view(['GET'])
# def movie_details(request,pk):
#     if request.method == 'GET':
#         list_name = WatchList.objects.get(pk=pk)
#         serializer_list = WatchListSerializer(list_name)
#         return Response(serializer_list.data)


# @api_view(['GET', 'POST'])
# def stream_list(request, format = None):
#     if request.method == 'GET':
#         stream_name = PlatForm.objects.all()
#         serializer_list = PlatFormSerializer(stream_name, many=True)
#         return Response(serializer_list.data)
    
#     elif request.method == 'POST':
#         data_from = request.data
#         serializered = PlatFormSerializer(data = data_from)
#         if serializered.is_valid():
#             serializered.save()
#             return Response(serializered.data,status= status.HTTP_201_CREATED)
#         return Response(serializered.errors , status= status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET','PUT','DELETE'])
# def stream_details(request,pk,format = None):
#     try:
#         stream_platform = PlatForm.objects.get(pk = pk)
#     except PlatForm.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = PlatFormSerializer(stream_platform)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = PlatFormSerializer(stream_platform, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
#     elif request.method == 'DELETE':
#         stream_platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class movie_list(APIView):
#     def get(self,format=None):
#         list_name = WatchList.objects.all()
#         serializer_list = WatchListSerializer(list_name, many=True)
#         return Response(serializer_list.data)

# class movie_details(APIView):
#     def get(self,request,pk,format= None):
#         list_name = WatchList.objects.get(pk=pk)
#         serializer_list = WatchListSerializer(list_name)
#         return Response(serializer_list.data) 
#     def put(self,pk,request,format=None):
#         movie_name = WatchList.objects.get(pk = pk)
#         serializer = WatchListSerializer(serializer,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


# class stream_list(APIView):
#     def get(self,request,format=None):
#         stream_name = PlatForm.objects.all()
#         serializer_list = PlatFormSerializer(stream_name, many=True)
#         return Response(serializer_list.data)
    
#     def post(self,request,format=None):
#         stream_name = PlatForm.objects.all()
#         serializer_list = PlatFormSerializer(data=request.data)
#         if serializer_list.is_valid():
#             serializer_list.save()
#             return Response(serializer_list.data,status=status.HTTP_201_CREATED)
#         return Response(serializer_list.errors,status=status.HTTP_400_BAD_REQUEST)
        
# class stream_details(APIView):
    
#     def get_object(self,pk):
#         try:
#             platform_name = PlatForm.objects.get(pk = pk)
#             return platform_name
#         except PlatForm.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
    
#     def put(self,request,pk,format = None):
#         platform_name = self.get_object(pk)
#         serializer = PlatFormSerializer(platform_name, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def get(self,request,pk,format = None):
#         platform_name = self.get_object(pk)
#         serializer = PlatFormSerializer(platform_name)
#         return Response(serializer.data)
    
#     def delete(self,request,pk,format= None):
#         Platform_name = self.get_object(pk)
#         serializer = PlatFormSerializer(Platform_name,data = request.data)
#         if serializer.is_valid():
#             serializer.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

class stream_list(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    queryset = PlatForm.objects.all()
    serializer_class = PlatFormSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    

class stream_details(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    #RetrieveModelMixin --> It can retrieve a single object 
    #by its primary key(e.g.,for an HTTP GET request)
    
    queryset = PlatForm.objects.all()
    serializer_class = PlatFormSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        return response

    def delete(self, request, *args, **kwargs):
        response =  self.destroy(request, *args, **kwargs)
        return response

class movie_list(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

class movie_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    

class movie_review(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist = pk)

class Review_create(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def perform_create(self,serializer):
        pk = self.kwargs['pk']
        movie = WatchList.objects.get(pk = pk)
        review_user = self.request.user
        review_quaryset = Review.objects.filter(review_user = review_user , watchlist = movie )
        if review_quaryset.exists():
            raise ValidationError('Review is already created!')
        serializer.save(watchlist = movie, review_user = review_user)
        return serializer

class review_List(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
class review_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        details = Review.objects.filter(pk = pk)
        return details
        
        