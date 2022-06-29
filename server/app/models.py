from django.db import models

class File(models.Model):
    file = models.FileField(upload_to='app/files')
    # def __str__(self):
    #     return self.user.username