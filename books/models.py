from django.db import models

class Book (models.Model):
    STATUS_CHOICES = [
        ('read', 'Reading'),
        ('reading', 'Currently reading'),
        ('to_read', 'To read' ),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True, null=True )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_read')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



