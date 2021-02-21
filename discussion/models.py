from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

class QA(models.Model):
    question = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)

    #slug = models.SlugField(max_length=200, blank=True)
    #def save(self, *args, **kwargs):
    #    if not self.slug:
    #        self.slug = slugify(self.question)
    #    super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('qeustionsandswers:question_detail', args=[self.id])
    
    def get_tags(self):
        """ names() is a django-taggit method, returning a ValuesListQuerySet 
        (basically just an iterable) containing the name of each tag as a string
        """
        return self.tags.names()

    class Meta:
        ordering = ['-created']

 
class Answer(models.Model):
    question = models.ForeignKey(QA,
                             on_delete=models.CASCADE,
                             related_name='answers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'reply by {self.user} on {self.qa}'
