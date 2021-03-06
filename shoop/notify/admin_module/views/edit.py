# -*- coding: utf-8 -*-
# This file is part of Shoop.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from shoop.admin.toolbar import Toolbar, URLActionButton
from shoop.admin.utils.views import CreateOrUpdateView, add_create_or_change_message
from shoop.notify.admin_module.forms import ScriptForm
from shoop.notify.models.script import Script


class ScriptEditView(CreateOrUpdateView):
    model = Script
    form_class = ScriptForm
    template_name = "notify/admin/edit_script.jinja"
    context_object_name = "script"

    def get_context_data(self, **kwargs):
        context = super(ScriptEditView, self).get_context_data(**kwargs)
        if self.object.pk:
            context["toolbar"] = Toolbar([
                URLActionButton(
                    text=_(u"Edit Script Contents..."),
                    icon="fa fa-pencil",
                    extra_css_class="btn-info",
                    url=reverse("shoop_admin:notify.script.edit-content", kwargs={"pk": self.object.pk})
                )
            ])
        return context

    def form_valid(self, form):
        is_new = (not self.object.pk)
        wf = form.save()
        if is_new:
            return redirect("shoop_admin:notify.script.edit-content", pk=wf.pk)
        else:
            add_create_or_change_message(self.request, self.object, is_new=is_new)
            return redirect("shoop_admin:notify.script.edit", pk=wf.pk)
