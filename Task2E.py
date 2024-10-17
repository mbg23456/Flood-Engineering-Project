from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels


def run():
    """
    Task 2E: Plot graphs to show the recent water level of chosen stations.
    """
    # build station list with updated water level
    stations=build_station_list()
    update_water_levels(stations)
    
    # get the 5 stations with highest water level
    sorted_stations_desc = sorted(stations, key=lambda x: x.latest_level if x.latest_level is not None else float('-inf'), reverse=True)
    first_five=sorted_stations_desc[:5]
    
    # plot water level against time
    dt=10
    #select each of the first five highest stations
    for element in first_five:
        #function below found in datafetcher
        dates, levels = fetch_measure_levels(element.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(element,dates,levels)



if __name__ == "__main__":
    print("*** Task 2E: Flood Warning System ***")
    run()