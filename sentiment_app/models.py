from django.db import models
from .utils import analyze_sentiment

# Create your models here.
class Feedback(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    sentiment = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return self.text[:100]
    
    def save(self, *args, **kwargs):
        self.sentiment = analyze_sentiment(self.text)
        super(Feedback, self).save(*args, **kwargs)