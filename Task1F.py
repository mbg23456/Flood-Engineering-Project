from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation


def run():
    """
    Task 1F: Isolate stations that do not have a water level high value greater than the minimum value.
    """

    #Create list of stations
    stations = build_station_list()

    
    #Show only the inconsistent stations
    print(MonitoringStation.inconsistent_typical_range(stations))



#make the task run
if __name__ == "__main__":
    print("*** Task 1F: Flood Warning System ***")
    run()