"""
Mapper of heart rate and power to a zone.
"""

import numpy as np

# import alt

class ZoneMapper:

    def __init__(self, data, log=None):
        self.data = data
        self.log = log

    def get_zone(self, field, zone):
        """Return the data for the given field and zone."""
        # get the data for the given field
        field_data = self.data[field]
        # get the zone limits
        zone_limits = self.get_zone_limits(field, zone)
        # get the data in the given zone
        zone_data = field_data[(field_data >= zone_limits[0]) & (field_data <= zone_limits[1])]
        return zone_data

    def get_zone_limits(self, field, zone):
        """Return the zone limits for the given field and zone."""
        # get the zone limits
        if field == 'heart_rate':
            if zone == 1:
                zone_limits = [0, 120]
            elif zone == 2:
                zone_limits = [121, 140]
            elif zone == 3:
                zone_limits = [141, 160]
            elif zone == 4:
                zone_limits = [161, 180]
            elif zone == 5:
                zone_limits = [181, 200]
            elif zone == 6:
                zone_limits = [201, 220]
            else:
                zone_limits = [0, 220]
        elif field == 'power':
            if zone == 1:
                zone_limits = [0, 100]
            elif zone == 2:
                zone_limits = [101, 200]
            elif zone == 3:
                zone_limits = [201, 300]
            elif zone == 4:
                zone_limits = [301, 400]
            elif zone == 5:
                zone_limits = [401, 500]
            elif zone == 6:
                zone_limits = [501, 600]
            else:
                zone_limits = [0, 600]
        else:
            zone_limits = [0, 0]
        return zone_limits

    def get_zone_duration(self, field, zone):
        """Return the duration of the given field and zone."""
        # get the data for the given field
        field_data = self.data[field]
        # get the zone limits
        zone_limits = self.get_zone_limits(field, zone)
        # get the data in the given zone
        zone_data = field_data[(field_data >= zone_limits[0]) & (field_data <= zone_limits[1])]