from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to='img')
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    