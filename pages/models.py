from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class FeedBack(models.Model):
    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message if len(self.message) < 50 else f'{self.message[:50]}.....' 

    class Meta:
        verbose_name_plural = 'feedback'