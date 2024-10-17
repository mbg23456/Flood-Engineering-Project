# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
#the haversine package can find the geodesic distance for us.
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    #aim is to return distance of each station from p
    #done as tuples: (station, distance)

    #first argument is the given station:
    #distance = haversine(stations, p)

    #now order these distances
    
    return sorted([(station, haversine(station.coord, p)) for station in stations], key = lambda x: x[1])

def stations_within_radius(stations, centre, r):
    """
    Function to find all of the stations within a radius of r from a point 'centre'.
    """


    return sorted([station for station in stations if haversine(station.coord, centre) <= r ],
                  key = lambda station : [haversine(station.coord, centre) for station in stations])

def rivers_with_station(stations):
    """
    Function to return a container with the names of rivers on which all given stations lie.
    """

    #We will create a set to avoid duplicate entries.
    #make the set alphabetical also.
    return sorted(set(station.river for station in stations))

def stations_by_river(stations):
    """
    Function to return list of stations associated with given rivers.
    """
    
    #create a dictionary
    rivdict = dict()
    for station in stations:
        if station.river in rivdict:
            rivdict[station.river] += [station.name]
        else:
            rivdict[station.river] = [station.name]
    return dict(sorted(rivdict.items()))


def rivers_by_station_number(stations,N):
    """ determines the N rivers with the greatest number of monitoring stations"""
    if type(N) != int:
        raise TypeError('Please input a valid integer')

    river_count = {}
    #count how many monitoring stations each river has
    for station in stations:
        if station.river not in river_count:
            river_count[station.river] = 1
        else:
            river_count[station.river] += 1
    
    #This turns the dict into a list of tuples, and sorts them by the number of stations but in reverse order

    sorted_rivers = sorted(river_count.items(), key=lambda x: x[1], reverse=True)

    Nth_entry = sorted_rivers[N-1][1] if N <= len(sorted_rivers) else 0

    result = [(river, count) for river, count in sorted_rivers if count >= Nth_entry]

    return result

    