from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import PROTECT


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Language(models.Model):
    """
    Language model containing languages that are available and required
    """
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Data(models.Model):
    """
    Data model responsible for receiving data input from contributor. The data can be either text file or
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, on_delete=PROTECT)
    text = models.TextField()
    file = models.FileField(blank=True, null=True, upload_to='files')
    approved = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.language.name
