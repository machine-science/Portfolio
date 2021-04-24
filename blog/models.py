from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    dody = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.dody[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
