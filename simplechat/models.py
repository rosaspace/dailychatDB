from django.db import models

class Conversation(models.Model):
    LEVEL_CHOICES = [
        ('beginner', '初级'),
        ('intermediate', '中级'),
        ('advanced', '高级'),
    ]
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

class Dialogue(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='dialogues', on_delete=models.CASCADE)
    english = models.TextField()
    chinese = models.TextField()
    order = models.IntegerField()

    class Meta:
        ordering = ['order']