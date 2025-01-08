from django.db import models

# Category model to define product categories (e.g., Electronics, Clothing)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Category name must be unique

    def __str__(self):
        return self.name


# Tag model to define product tags (e.g., New, Sale, Popular)
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Tag name must be unique

    def __str__(self):
        return self.name


# Product model to define the products themselves
class Product(models.Model):
    name = models.CharField(max_length=200)  # Name of the product
    description = models.TextField()  # Description of the product
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)  # Link to Category (can't be null or blank)
    tags = models.ManyToManyField(Tag, blank=True)  # Many-to-many relation with Tag, can be blank (product might have no tags)

    def __str__(self):
        return self.name
