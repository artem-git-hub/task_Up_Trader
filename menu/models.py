from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=255, null=True, blank=True)

    
    def __str__(self):
        return str(f"Title: {self.title}; URL: {self.url}")
