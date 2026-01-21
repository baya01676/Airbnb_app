from symtable import Class

from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    RoleChoices = (
        ('guest', 'guest'),
        ('host', 'host'),
        ('admin', 'admin')
    )
    role = models.CharField(max_length=20, choices=RoleChoices, default='guest')
    phone_number = PhoneNumberField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)


class City(models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name


class Rules(models.Model):
    RulesChoices = (
        ('no_smoking', 'no_smoking'),
        ('pets_allowed', 'pets_allowed'),
        ('etc', 'etc')
    )
    rules_name = models.CharField(max_length=64, choices=RulesChoices)

    def __str__(self):
        return self.rules_name


class Guest(models.Model):
    guest_name = models.CharField(max_length=50)
    guest_image = models.ImageField(upload_to='rules_image', null=True, blank=True)

    def __str__(self):
        return self.guest_name

class Property(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    price_per_night = models.PositiveSmallIntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')
    address = models.CharField(max_length=100)
    PropertyTypeChoices = (
        ('apartment', 'apartment'),
        ('house', 'house'),
        ('studio', 'studio')
    )
    property_type = models.CharField(max_length=20, choices=PropertyTypeChoices)
    rules = models.ManyToManyField(Rules, related_name='rules')
    max_guests = models.PositiveSmallIntegerField()
    max_bedrooms = models.PositiveSmallIntegerField()
    max_bathrooms = models.PositiveSmallIntegerField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="properties")
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.title}, {self.description}, {self.address}'

    def get_avg_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum([i.rating for i in reviews]) / reviews.count(), 1)
        return 0

    def get_count_people(self):
        return self.reviews.count()

    def get_price_property(self):
        return self.price_per_night * 2

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE,related_name='property_image')
    image = models.ImageField(null=True, blank=True)


class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    quest = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    StatusTypeChoices = (
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
        ('cancelled', 'cancelled')
    )
    status = models.CharField(max_length=30, choices=StatusTypeChoices)

    def __str__(self):
        return f'{self.status}'


class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE,related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.comment


class Amenity(models.Model):
    name = models.CharField()
    icon = models.ImageField(upload_to='icons_images')
    property = models.ManyToManyField(Property)

    def __str__(self):
        return self.name