from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Card(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='cards')
    position = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['position']
