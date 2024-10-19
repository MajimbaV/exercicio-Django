from django.db import models

# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=100)
    max_HP = models.PositiveIntegerField()
    base_AC = models.PositiveIntegerField()
    mana = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.name
        
class Item(models.Model):
    name = models.CharField(max_length=100)
    effect = models.TextField()
    
    def __str__(self) -> str:
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100)
    player_name = models.CharField(max_length=100)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name="+")
    inventory = models.ManyToManyField(Item, related_name="+")
    
    def __str__(self) -> str:
        return self.name
        