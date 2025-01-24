from rest_framework import  serializers
from .models import PlatForm
from .models import WatchList
from .models import Review

# class WatchListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=50)
#     storyline = serializers.CharField(max_length=100)
#     active = serializers.BooleanField(default=True)
#     created = serializers.DateTimeField()
    
#     def create(self, validated_data):
#         """
        
#         Create and return a new `PlatForm` instance, given the validated data.
#         """
        
#         return WatchList.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update and return existing 'PlatForm' instance,given the validate data.
#         """
#         #instance = old data 
#         #validate = new data
        
#         instance.title = validated_data.get('title',instance.title)
#         instance.storyine = validated_data.get('storyline',instance.storyline)
#         instance.active = validated_data.get('active',instance.active)
#         instance.created = validated_data.get('created',instance.created)
#         instance.save()
        
#         return instance
  
     
class WatchListSerializer(serializers.ModelSerializer):
    platform = serializers.ReadOnlyField(source = 'platform.name')

    class Meta:
        model = WatchList
        fields = ['id','title','storyline','platform','active','created']



class PlatFormSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='stream_details')
   # watch_related = WatchListSerializer(many = True, read_only = True)
    watch_related = serializers.StringRelatedField(many=True,read_only = True)
    class Meta:
        model = PlatForm
        fields = '__all__' 
# class PlatFormSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50)
#     about = serializers.CharField(max_length=100)
#     website = serializers.URLField(max_length=30)
    
#     def create(self, validated_data):
#         """
#         Create and return a new `PlatForm` instance, given the validated data.
#         """
#         return PlatForm.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `PlatForm` instance, given the validated data.
#         """
#         # Update only the fields that exist in `validated_data`
#         instance.name = validated_data.get('name', instance.name)
#         instance.about = validated_data.get('about', instance.about)
#         instance.website = validated_data.get('website', instance.website)
#         instance.save()
#         return instance

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'