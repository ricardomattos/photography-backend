from django.db import models


def post_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'post_{0}/{1}'.format(instance.owner.id, filename)


class Post(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Image(models.Model):
    owner = models.ForeignKey('Post', on_delete=models.CASCADE)
    #image = models.ImageField(upload_to=post_directory_path)

    image = models.BinaryField(blank=False)
