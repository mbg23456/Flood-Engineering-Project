# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
#
#Based on a Cambridge University Engineering Group Project

from floodsystem.stationdata import build_station_list


def run():
    """
    Task 1A prints a sample of the station list.
    """

    # Build list of stations
    stations = build_station_list()

    # Print number of stations
    print("Number of stations: {}".format(len(stations)))

    # Display data from 3 stations:
    for station in stations:
        if station.name in [
                'Bourton Dickler', 'Surfleet Sluice', 'Gaw Bridge'
        ]:
            print(station)


if __name__ == "__main__":
    print("*** Task 1A: Flood Warning System ***")
    run()
