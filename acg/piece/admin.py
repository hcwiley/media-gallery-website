from django.contrib import admin
from piece.models import *

class MyImageAdmin(admin.ModelAdmin):
    actions = [update_thumbs]
    class Meta:
        model = MyImage

class PieceAdmin(admin.ModelAdmin):
    class Meta:
        model = Piece

admin.site.register(MyImage, MyImageAdmin)
admin.site.register(Piece, PieceAdmin)
