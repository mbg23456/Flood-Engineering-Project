from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """
    Task 1B sorts the  stations by distance.
    """
    #ask for p
    #Take p as Cambridge City Centre
    p = (52.2053, 0.1218)


    # Find the distance between stations
    #distances = stations_by_distance()
    #print(distances)

    # Build list of stations
    stations = build_station_list()

    # Print number of stations
    print("Number of stations: {}".format(len(stations)))

    #full list: 
    #print('order is : ', stations_by_distance(stations, p))
    sorted_stations = stations_by_distance(stations, p)
    # Print nearest stations and their distances
    print([(s[0].name, s[0].town, s[1]) for s in sorted_stations[:10]])


#make the task run
if __name__ == "__main__":
    print("*** Task 1B: Flood Warning System ***")
    run()