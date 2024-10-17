from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level



def run():
    """
    Task 2C: Return the N most at risk stations.
    """
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    N_most_flooded = stations_highest_rel_level(stations, 10)

    print(N_most_flooded)
if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
