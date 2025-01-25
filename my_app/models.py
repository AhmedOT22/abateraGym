from django.db import models

# Represents gym services (e.g., personal training, yoga, Zumba classes)
class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# Represents members of the gym
class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    join_date = models.DateField(auto_now_add=True)
    membership_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Represents trainers/instructors at the gym
class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    expertise = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.expertise}"


# Represents gym classes (e.g., Zumba, Yoga)
class GymClass(models.Model):
    name = models.CharField(max_length=100, unique=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="classes")
    start_time = models.TimeField()
    end_time = models.TimeField()
    days_of_week = models.CharField(max_length=50)  # e.g., "Monday, Wednesday, Friday"
    max_capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} by {self.trainer}"


# Represents membership plans (e.g., Basic, Premium)
class MembershipPlan(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.PositiveIntegerField()  # e.g., 1, 3, 12

    def __str__(self):
        return f"{self.name} - {self.price}/month"


# Represents a member's subscription to a membership plan
class Subscription(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="subscriptions")
    membership_plan = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return f"{self.member} - {self.membership_plan}"


# Represents a booking for a gym class
class ClassBooking(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="bookings")
    gym_class = models.ForeignKey(GymClass, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.member} - {self.gym_class}"
