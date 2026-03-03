import datetime

from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels

def main_2E():
    # get updated station list
    stations = build_station_list()
    update_water_levels(stations)

    # get 5 stations with highest current water levels
    high_stations = [station_pkg[0] for station_pkg in stations_highest_rel_level(stations, 5)]

    # get data from past 10 days
    dt = 10

    for station in high_stations:
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        
        

if __name__ == '__main__':
    main_2E()