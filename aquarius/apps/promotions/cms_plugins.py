from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import PromotionPlugin
from django.utils.translation import ugettext as _

class CMSPromotionPlugin(CMSPluginBase):
    model = PromotionPlugin
    name = _("Promotion")
    render_template = "promotion.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(CMSPromotionPlugin)