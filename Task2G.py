from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation

from floodsystem.plot import get_water_level_fit

import matplotlib.dates as pdt
import matplotlib.pyplot as plt

import numpy as np

import datetime 

def init() -> list[MonitoringStation]:
    stations = build_station_list(use_cache=True)
    update_water_levels(stations)

    return stations

# def get_level_gradient()


def forecast_water_level_sign(station, short, long) -> None:
    print(f"Fetching measure levels for station {station.name} at {station.town} measuring {station.river} ...")
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(long))
    if dates == [] or levels == []:
        return (None, None)

    print(f"Obtaining linear fit for data for station {station.name} ...")
    poly_l, _ = get_water_level_fit(dates, levels, 1)
    coeff_l = poly_l.coefficients[0]

    timescale_factor = round(len(dates)/(long/short))
    poly_s, _ = get_water_level_fit(dates[:timescale_factor], levels[:timescale_factor], 1)
    coeff_s = poly_s.coefficients[0]

    return (np.sign(coeff_l if abs(coeff_l) > 0.05 else 0), 
            np.sign(coeff_s if abs(coeff_s) > 0.05 else 0))

def evaluate_flooding(station) -> tuple[float, str]:
    frwl_short, frwl_long = forecast_water_level_sign(station, 0.5, 10)
    rwl = station.relative_water_level()

    if any([q == None for q in (frwl_short, frwl_long, rwl)]):
        print(f'[{station.name.upper()}] Incomplete information for this station')
        return (None, None)
    
    # calibration factors
    rwl_factor = 0.1
    rwl_augment = 0.35

    short_grad_factor = 0.1 + (0.4 if rwl > 0.7 else 0)
    long_grad_factor = 0.005

    # score evaluation
    score = ( (rwl) * (rwl_factor + (rwl_augment if rwl > 0.7 else 0)) + 
                ((frwl_short + (0.90 if rwl > 1 else 0))) * short_grad_factor + 
                frwl_long * long_grad_factor) / \
    (rwl_factor + short_grad_factor + long_grad_factor + (rwl_augment if rwl > 0.7 else 0))

    print(f'[{station.name.upper()}] short term water level: {'rising' if frwl_short > 0 else 'falling' if frwl_short < 0 else 'steady'}')
    print(f'[{station.name.upper()}]  long term water level: {'rising' if frwl_long > 0 else 'falling' if frwl_long < 0 else 'steady'}')
    print(f'[{station.name.upper()}] water level {rwl*100}% of nominal range')

    print(f'[{station.name.upper()}] nominal range of levels: {station.typical_range}')
    print(f'[{station.name.upper()}] measured water level: {station.latest_level}')

    status = 'LOW/NONE' if score < 0.05 else \
            'MODERATE' if 0.05 <= score < 0.10 else \
            'HIGH' if 0.10 <= score < 0.25 else \
            'SEVERE'

    return score, status

def main() -> None:
    stations = init()
    print("initial setup complete")

    warning_stations = [station_data[0] for station_data in stations_level_over_threshold(stations, 0.3)]
    print(f'Testing {len(warning_stations)} higher-risk stations ...\n\n')

    for station in stations[250:265]:
        score, status = evaluate_flooding(station)
        
        # report
        print(f'[{station.name.upper()}]\'s flood score: {None if score is None else score*100}')
        print(f'[{station.name.upper()}] flood status: {status}\n')

if __name__ == '__main__':
    main()