# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    #this function prints a description of the station
    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        d += "   latest level:  {}".format(self.latest_level)
        return d

    #Check for consistency in ranges
    def typical_range_consistent(self):
        "Inconsistent range if high value < low value, or if no value"
        if self.typical_range is None:
            return False
        elif self.typical_range[0] > self.typical_range[1]:
            return False

        else:
            return True
    
    def relative_water_level(self):
        "Return the latest water level as a fraction of the typical range, i.e. 1.0 is at a typical high etc."
        if self.typical_range_consistent() == False or self.latest_level == None or self.latest_level <0:
            return None
        else:
            #[0] index is range low, [1] is high
            low_level = self.typical_range[0]
            high_level = self.typical_range[1]
            water_level_ratio = (self.latest_level - low_level) / (high_level - low_level)
            return water_level_ratio

    def inconsistent_typical_range(stations):
        "Add the station to an alphabetical list if it is not consistent"
        inconsistent_stations = []
        for station in stations:
            if MonitoringStation.typical_range_consistent(station) == True:
                pass
            else:
                inconsistent_stations.append(station.name)

        return sorted(inconsistent_stations)


def call_typical_range_consistent(station):
    "Useful if we need to call whether a station is consistent"
    return station.typical_range_consistent()

def call_relative_water_level(station):
    return station.relative_water_level()
