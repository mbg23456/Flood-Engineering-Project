from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    """Task 1D: Prints rivers associated with a given station."""

    #Create list of stations
    stations = build_station_list()

    #rivers by station
    rivers_set = rivers_with_station(stations)

    #print the first ten rivers
    print(list(rivers_set)[:10])

    #stations by river
    stations_dict = stations_by_river(stations)

    #print stations associated with three rivers
    print(stations_dict['River Aire'])
    print(stations_dict['River Cam'])
    print(stations_dict['River Thames'])



#make the task run
if __name__ == "__main__":
    print("*** Task 1D: Flood Warning System ***")
    run()