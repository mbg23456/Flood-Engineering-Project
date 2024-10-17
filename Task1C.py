from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    """
    Task 1C: Find and list stations within a given radius of an arbitrary coordinate.
    """
    #ask for p
    #Take centre as Cambridge City Centre
    centre = (52.2053, 0.1218)

    #choose radius of 5 km
    r = 5


    # Build list of stations
    stations = build_station_list()

    #full list: 
    #print('order is : ', stations_by_distance(stations, p))
    within_radius = stations_within_radius(stations, centre, r)
    # Print nearest stations and their distances
    #sorted(within_radius, key = lambda station: [station.coord for station in stations])
    print(within_radius)


#make the task run
if __name__ == "__main__":
    print("*** Task 1C: Flood Warning System ***")
    run()