from django.db import models
from django.contrib.auth.models import User

# Reader model 
class Reader(models.Model):
    user = models.OneToOneField(User, related_name="reader", on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'username - {}'.format(self.user.username)    
    class Meta:
        ordering = ["-join_date"]

# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Reader, on_delete=models.SET_NULL, null=True, related_name="books")
    genre = models.CharField(max_length=200)
    amazon_url = models.URLField(max_length = 200)  
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title


