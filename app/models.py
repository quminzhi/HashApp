from django.db import models
import uuid

# Create your models here.

class App(models.Model):
    KIND_CHOICE = (
        ('App', 'app'),
        ('API', 'api'),
        ('Design', 'design'),
        ('Server', 'server'),
    )

    PAGE_CHOICE = (
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6'),
        ('seven', '7'),
        ('eight', '8'),
        ('nine', '9'),
        ('ten', '10')
    )

    name = models.CharField(max_length=100, null=True, blank=True)
    kind = models.CharField(max_length=100, choices=KIND_CHOICE)
    page_no = models.CharField(
        max_length=100, null=True, blank=True, choices=PAGE_CHOICE)
    intro = models.TextField(null=True, blank=True)
    # root of media url: static/images/
    image = models.ImageField(
        null=True, blank=True, upload_to='app/featured-image/', default="app/default.jpg")
    link = models.CharField(max_length=200, null=True, blank=True)
    github = models.CharField(max_length=200, null=True, blank=True)
    hasDoc = models.BooleanField(null=True, blank=True, default=False)

    docname = models.CharField(max_length=200, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Art(models.Model):
    nickname = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    origin_image = models.ImageField(
        null=True, blank=True, upload_to='webapp/byte-art/', default="webapp/default-origin.jpg")
    style_image = models.ImageField(
        null=True, blank=True, upload_to='webapp/byte-art/', default="webapp/default-style.jpg")

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.nickname

    class Meta:
        ordering = ['-created']

    @property
    def originImageURL(self):
        try:
            url = self.origin_image.url
        except:
            url = ''
        return url
        
    @property
    def styleImageURL(self):
        try:
            url = self.style_image.url
        except:
            url = ''
        return url