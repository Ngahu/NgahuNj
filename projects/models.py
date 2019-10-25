import uuid
from django.db import models
from tinymce import HTMLField
from ngahunj.core.utils import unique_slug_generator
from django.conf import settings
from django.db.models.signals import pre_save

User = settings.AUTH_USER_MODEL


def tech_used_upload(instance, filename):
    return "technologies-used/%s/%s" % (instance.name, filename)


class Technology(models.Model):
    """
    A Technology is a tool that I use in my software development world.
    """
    name = models.CharField(max_length=100)
    internal_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    description = models.TextField(blank=True)
    image_icon = models.FileField(upload_to=tech_used_upload, blank=True, null=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technologies Used"
        ordering = ["-date_created"]


def project_upload(instance, filename):
    return "%s/%s" % (instance.title, filename)


class Project(models.Model):
    """
    A Project is something i have worked on.
    """
    title = models.CharField(max_length=120)
    internal_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    featured = models.BooleanField(default=False)
    project_client = models.CharField(max_length=100, blank=True, null=True)
    project_type = models.CharField(max_length=120, blank=True, null=True)
    description = HTMLField('Content')
    related_article = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=250)
    image = models.ImageField(upload_to=project_upload, blank=True, null=True)
    image_1 = models.ImageField(upload_to=project_upload, blank=True, null=True)
    image_2 = models.ImageField(upload_to=project_upload, blank=True, null=True)
    image_3 = models.ImageField(upload_to=project_upload, blank=True, null=True)
    image_4 = models.ImageField(upload_to=project_upload, blank=True, null=True)
    category = models.CharField(max_length=100)
    technologies_used = models.ManyToManyField('Technology', blank=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Projects"
        ordering = ["-updated", "date_created"]

    def get_absolute_url(self):
        pass


def project_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(project_pre_save_receiver, sender=Project)
