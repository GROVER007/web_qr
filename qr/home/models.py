from django.db import models

# Create your models here.
class Feedback(models.Model):
    
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122)
    email = models.EmailField(max_length=222)
    comment = models.TextField(default = "comment")
    date = models.DateField()
    
    def __str__(self):
        return self.fname +""+self.lname