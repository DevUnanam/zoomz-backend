from django.db import models
from django.contrib.auth.models import User


# Dealership Model
class Dealership(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Rating out of 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Car Model
class Car(models.Model):
    make = models.CharField(max_length=100)  # e.g., Toyota, Ford
    model = models.CharField(max_length=100)  # e.g., Corolla, F-150
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the car
    description = models.TextField()
    mileage = models.IntegerField(null=True, blank=True)  # Miles driven, optional
    location = models.CharField(max_length=255)  # Location of the car
    is_available = models.BooleanField(default=True)  # Whether the car is available
    dealership = models.ForeignKey(
        'Dealership', on_delete=models.CASCADE, related_name="cars"
    )  # Link to the dealership
    thumbnail_image = models.ImageField(upload_to='car_images/', blank=True, null=True)  # Rename field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


# Car Image Model
class CarImage(models.Model):
    car = models.ForeignKey(
        Car, related_name='images', on_delete=models.CASCADE
    )  # Keep related_name='images'
    image = models.ImageField(upload_to='car_images/')
    is_primary = models.BooleanField(default=False)  # To mark the primary image for the car

    def __str__(self):
        return f"{self.car.make} {self.car.model} - Image"


# Contact Inquiry Model
class ContactInquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry for {self.car} by {self.user.username}"


# Review Model (User Reviews for Cars and Dealerships)
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.car or self.dealership}"


# Car Filter Model (Optional, for storing filter criteria)
class CarFilter(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year_min = models.IntegerField()
    year_max = models.IntegerField()
    price_min = models.DecimalField(max_digits=10, decimal_places=2)
    price_max = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Filter for {self.make} {self.model}"


# Admin User Model (Optional for managing admin users)
class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


# Search History Model (Optional, for personalized searches)
class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search_criteria = models.JSONField()  # Store search filters as a JSON object
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Search history for {self.user.username}"

# FAQ Model for the Chatbot
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question