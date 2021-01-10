from djongo import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    class Meta:
        abstract = True


class Entry(models.Model):
    blog = models.EmbeddedField(model_container=Blog,)
    headline = models.CharField(max_length = 255)
    objects = models.DjongoManager()

    def __str__(self):
        return str(self.blog) + str(self.headline)