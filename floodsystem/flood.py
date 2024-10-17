from floodsystem.station import call_relative_water_level
from .station import call_typical_range_consistent
def stations_level_over_threshold(stations, tol):
    "Return a tuple of each station and its relative water level (must be above tol)"
    valid_stations = []
    for station in stations:
        if call_typical_range_consistent(station) is True:
            valid_stations.append(station)

    risk_stations = []
    for station in valid_stations:
        level = call_relative_water_level(station)
        if level != None:
            if level > tol:
                risk_stations.append((station.name, level))

    
    sorted_risk_stations = sorted(risk_stations, key=lambda x: x[1], reverse=True)

    return sorted_risk_stations

def stations_highest_rel_level(stations, N):
    "Return a list of N stations at which the relative water level is highest."
    
    #We choose the N highest values using the previous function

    return stations_level_over_threshold(stations, 0)[:N]
