from django.contrib import admin
from .models import (
    Post,
    ResourceCS,
    ResourceTh,
    ResourceDs,
    ResourceCe,
    ResourceAlg,
    ResourceAlg_Graphs,
    ResourceGraphs
)
# Register your models here. to show up on admin page

# adds Post access in gui for admin like adding and editing users
admin.site.register(Post)
admin.site.register(ResourceCS)
admin.site.register(ResourceTh)
admin.site.register(ResourceDs)
admin.site.register(ResourceCe)
admin.site.register(ResourceAlg)
admin.site.register(ResourceAlg_Graphs)
admin.site.register(ResourceGraphs)
