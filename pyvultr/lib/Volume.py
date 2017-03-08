# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from .baseapi import BaseAPI

class Volume(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.subid = None
        self.date_created = None
        self.cost_per_month = None
        self.status = None
        self.size_gb = None
        self.dcid = None
        self.attached_to_subid = None
        self.label = None

        super(Volume, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, api_token, volume_id):
        """
        Class method that will return an Volume object by ID.
        """
        volume = cls(token=api_token, subid=volume_id)
        volume.load()
        return volume

    def load(self):
        """
        Documentation: https://www.vultr.com/api/#block_block_list
        """
        volumes = self.get_data("block/list")

        for volume in volumes:
            if volume["SUBID"] == self.subid:
                for attr in volume.keys():
                    setattr(self, attr, volume[attr])

    def create(self, *args, **kwargs):
        """
        Creates a Block Storage Volume.

        Args:
            dcid: integer - DCID of the location to create this subscription in.
            size_gb: integer - Size in GB of this subscription.

        Optional Args:
            label: string - Text Label that will be associated with this subscription.
        """
        input_params = {
            'dcid': self.dcid,
            'size_gb': self.size_gb,
            'label': self.label
        }

        data = self.get_data(
            "block/create",
            type=POST,
            params=input_params
        )

        if data:
            self.subid = data['SUBID']
