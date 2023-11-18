from django.db import models

class PkMnyNote(models.Model):
    item  = models.CharField( max_length=100)
    price = models.IntegerField()
    notes = models.TextField()  # お小遣い説明やメモ

    def __str__(self):
        return f"ID:{self.id} item:{self.item} price:{self.price}"
