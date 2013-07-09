from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from models import Promotion

class PromotionInline(admin.StackedInline):
    model = Promotion
    extra = 0

class PromotionAdmin(admin.ModelAdmin):
    inlines = [PromotionInline]


admin.site.register(Promotion, PromotionAdmin)