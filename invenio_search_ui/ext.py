# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""UI for Invenio-Search."""

from __future__ import absolute_import, print_function

from . import config
from .views import blueprint


class InvenioSearchUI(object):
    """Invenio-Search-UI extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.register_blueprint(blueprint)
        app.extensions['invenio-search-ui'] = self

    def init_config(self, app):
        """Initialize configuration."""
        app.config.setdefault(
            'SEARCH_UI_BASE_TEMPLATE',
            app.config.get('BASE_TEMPLATE', 'invenio_search_ui/base.html')
        )
        app.config.setdefault(
            'SEARCH_UI_HEADER_TEMPLATE',
            app.config.get('HEADER_TEMPLATE',
                           'invenio_search_ui/base_header.html')
        )
        for k in dir(config):
            if k.startswith('SEARCH_UI_'):
                app.config.setdefault(k, getattr(config, k))
