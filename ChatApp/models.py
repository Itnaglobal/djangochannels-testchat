from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PrivateChtRoom(models.Model):
    room_name = models.CharField(max_length=220)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2")

    def __str__(self):
        return f"This is the chat between {self.user1} and {self.user2}"


class Message(models.Model):
    room = models.ForeignKey(PrivateChtRoom, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    # attachment = models.FileField(upload_to="files/")


    def __str__(self):
        return f"Private Chat room name: {self.room}"
