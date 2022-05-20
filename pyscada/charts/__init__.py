# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pyscada

__version__ = '0.7.0rc23'
__author__ = 'Madiane Gonnel'

default_app_config = 'pyscada.charts.apps.PyScadaChartsConfig'

PROTOCOL_ID = 72

parent_process_list = [{'pk': PROTOCOL_ID,
                        'label': 'pyscada.charts',
                        'process_class': 'pyscada.charts.worker.Process',
                        'process_class_kwargs': '{"dt_set":30}',
                        'enabled': True}]
