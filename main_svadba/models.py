from django.db import models


class GuestResponse(models.Model):

    name = models.CharField(max_length=100)

    will_come = models.BooleanField()

    alcohol = models.JSONField(default=list)

    alcohol_comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.name