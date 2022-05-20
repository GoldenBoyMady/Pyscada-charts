# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PyScadaChartsConfig(AppConfig):
    name = 'pyscada.charts'
    verbose_name = _("PyScada CHARTS loader")
    path = os.path.dirname(os.path.realpath(__file__))

    def ready(self):
        import pyscada.charts.signals
