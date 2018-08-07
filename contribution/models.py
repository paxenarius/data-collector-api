from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import PROTECT
from django.forms import ValidationError


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Language(models.Model):
    """
  Language model containing languages that are available and required
  """
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Data(models.Model):
    """
  Data model responsible for receiving data input from contributor. The data can be either text file or
  """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, on_delete=PROTECT)
    text = models.TextField(blank=True, null=True)
    file = models.FileField(
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['pdf', 'docx', 'doc'])],
        verbose_name='File: (Only pdf, docx or doc files with a maximum size of 2MB are allowed.)',
    )
    approved = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def save(self, **kwargs):
        self.clean()
        if self.approved == True:
            from ajiragis_api.opay import make_deposit
            make_deposit(1)
        return super().save(**kwargs)

    def clean(self):
        if self.text and self.file:
            raise ValidationError('Provide only either text or file')
        if not self.text and not self.file:
            raise ValidationError('Enter text or select file to upload')

    def __str__(self):
        return self.language.name
