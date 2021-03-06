# -*- coding: utf-8 -*-
# This file is part of Shoop.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from jsonfield import JSONField

from ._base import ShoopModel
from .shops import Shop


@python_2_unicode_compatible
class ConfigurationItem(ShoopModel):
    shop = models.ForeignKey(Shop, related_name="+", null=True, blank=True, on_delete=models.CASCADE)
    key = models.CharField(verbose_name=_("key"), max_length=100)
    value = JSONField(verbose_name=_("value"))

    class Meta:
        unique_together = [("shop", "key")]
        verbose_name = _("configuration item")
        verbose_name_plural = _("configuration items")

    def __str__(self):
        if self.shop:
            return _("%(key)s for shop %(shop)s") % vars(self)
        else:
            return _("%(key)s (global)") % vars(self)

    def __repr__(self):
        return '<%s "%s" for %r>' % (type(self).__name__, self.key, self.shop)
