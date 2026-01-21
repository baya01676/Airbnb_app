from rest_framework import serializers
from .models import (
    UserProfile, City, Rules, Guest, Property, Amenity,
    PropertyImage, Booking, Review
)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

class  UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
       model = UserProfile
       fields = ['first_name', 'last_name', 'avatar','role' ]

class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
       model = UserProfile
       fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','city_name']


class RulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = '__all__'


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'


class PropertyDetailSerializer(serializers.ModelSerializer):
    property_image = PropertyImageSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = ['property_image','city','address','description','rules'
            ,'max_guests','max_bedrooms','max_bathrooms','title']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class PropertyListSerializer(serializers.ModelSerializer):
    property_image = PropertyImageSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()
    get_price_property = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True)
    city = CitySerializer()
    rules = RulesSerializer(many=True)

    class Meta:
        model = Property
        fields = ['property_image', 'price_per_night', 'title', 'avg_rating', 'count_people','reviews',
                  'get_price_property','city','rules']


    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()

    def get_price_property(self ,obj):
        return obj.get_price_property()

class CityDetailSerializer(serializers.ModelSerializer):
    city_property = PropertyListSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['city_name', 'city_property']


