from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    """
    Task 1E: List rivers by number of stations (print the first few).
    """

    #Create list of stations
    stations = build_station_list()


    stations_number = rivers_by_station_number(stations, 12)

    print(stations_number)




#make the task run
if __name__ == "__main__":
    print("*** Task 1E: Flood Warning System ***")
    run()