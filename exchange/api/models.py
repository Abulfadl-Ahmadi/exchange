from django.db import models


class Book(models.Model):
    title = models.CharField(max_length= 256)
    slug = models.SlugField(max_length= 256, unique=True)
    author = models.CharField(max_length=256)
    pages = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    length = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    front_cover = models.ImageField()
    back_cover = models.ImageField()
    spine = models.ImageField()
    properties = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def front_cover_url(self):
        if self.front_cover and hasattr(self.front_cover, 'url'):
            return self.front_cover.url
        
    @property
    def back_cover_url(self):
        if self.back_cover and hasattr(self.back_cover, 'url'):
            return self.back_cover.url
        
    @property
    def spine_url(self):
        if self.spine_url and hasattr(self.spine_url, 'url'):
            return self.spine.url
        
    @property
    def properties_url(self):
        if self.properties and hasattr(self.properties, 'url'):
            return self.properties.url
        
        