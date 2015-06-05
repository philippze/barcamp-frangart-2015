from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import IframePluginModel


class IframePlugin(CMSPluginBase):
    model = IframePluginModel
    name = 'Iframe'
    render_template = 'talk/iframe.html'

plugin_pool.register_plugin(IframePlugin)
