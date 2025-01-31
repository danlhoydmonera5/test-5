from django.db import models
from django.conf import settings
from django.urls import reverse



class Pet(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Adopted', 'Adopted'),
        ('Pending', 'Pending'),
    ]

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)  # Dog, Cat, Rabbit, etc.
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(help_text="Age in years")
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    description = models.TextField()
    photo = models.ImageField(upload_to='pet_photos/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return f"{self.name} ({self.species})"

    def get_absolute_url(self):
        return reverse('pet_detail', kwargs={'pk': self.pk})


# 3. Adoption Application Model
class AdoptionApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='applications')
    application_date = models.DateTimeField(auto_now_add=True)
    reason_for_adoption = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.applicant.username} - {self.pet.name} ({self.status})"

    def get_absolute_url(self):
        return reverse('application_detail', kwargs={'pk': self.pk})


# 4. Adoption Event Model
class AdoptionEvent(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=300)
    event_date = models.DateTimeField()
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('adoption_event_detail', kwargs={'pk': self.pk})


# 5. (Optional) Donation Model
class Donation(models.Model):
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.donor.username} - ₱{self.amount}"

    def get_absolute_url(self):
        return reverse('donation_detail', kwargs={'pk': self.pk})