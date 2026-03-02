from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
# Import my functions
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
import matplotlib.pyplot as plt
import datetime

def run():
    # # Build the list of MonitoringStation objects that will be input to my function
    stations = build_station_list()
    # Update water levels
    update_water_levels(stations)

    # Get 5 stations with current highest relative water level
    highest_stations = stations_highest_rel_level(stations, 5)

    # Set time frame
    time_frame = datetime.timedelta(days=2)

    # Get data and plot for each station
    for station, _ in highest_stations:
        dates, levels = fetch_measure_levels(station.measure_id, time_frame)

        # Assure reasonable result for no data
        if not dates or not levels:
            print(f"No data for {station.name}")
            continue

        print(f"Plotting: {station.name}")
        plot_water_level_with_fit(station, dates, levels, p=4)

if __name__ == "__main__":
    run()

