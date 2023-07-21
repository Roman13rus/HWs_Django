from django.db import models

# `id`, `name`, `price`, `image`, `release_date`, `lte_exists` и `slug`

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length = 50, null=False, unique=True)
