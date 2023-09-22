from django.db import models

class Item(models.Model):
    text = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.text