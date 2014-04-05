from rest_framework import serializers

from apps.yemekler.models import FoodCategory, Food


class FoodCategorySerializer(serializers.HyperlinkedModelSerializer):

    imagepath = serializers.Field(source='image_full_path')
    
    class Meta:
        model = FoodCategory
        fields = ('name', 'description', 'category_type', 'image' , 'imagepath')


class FoodSerializer(serializers.HyperlinkedModelSerializer):

    imagepath = serializers.Field(source='image_full_path')

    class Meta:
        model = Food
        fields = ('name', 'description', 'foodcategory', 'image', 'imagepath', 'recipe_url')


