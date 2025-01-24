from django.contrib import admin
from .models import PlatForm
from .models import WatchList
from .models import Review
# Register your models here.
admin.site.register(PlatForm)
admin.site.register(WatchList)
admin.site.register(Review)