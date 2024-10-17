
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    """
    Task 2B: Return stations whose level is above an arbitrary tolerance level (currently 3)."""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    over_threshold = stations_level_over_threshold(stations, 3)

    print(over_threshold)
if __name__ == "__main__":
    print("*** Task 2B: Flood Warning System ***")
    run()
