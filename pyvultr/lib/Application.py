# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals
try:
    from future.utils import iteritems
except ImportError:
    from six import iteritems

from .baseapi import BaseAPI

class Application(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.appid = None
        self.name = None
        self.short_name = None
        self.deploy_name = None
        self.surcharge = None

        super(Application, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, api_token, app_name):
        """
            Class method that will return a Application object by Name.
        """
        app = cls(token=api_token, name=app_name)
        app.load()
        return app

    def load(self):
        """
            Documentation: https://www.vultr.com/api/#app_app_list
        """
        apps = self.get_data("app/list")
        for app, description in iteritems(apps):
            if description["name"] == self.name:
                setattr(self, attr, description[attr])

    def __str__(self):
        return "<Application: %s>" % (self.name)
