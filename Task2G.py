from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation

from floodsystem.plot import get_water_level_fit

import matplotlib.dates as pdt
import matplotlib.pyplot as plt

import numpy as np

import datetime 

from pprint import pprint

def init() -> list[MonitoringStation]:
    stations = build_station_list(use_cache=True)
    update_water_levels(stations)

    return stations

# def get_level_gradient()


def forecast_water_level_sign(station, short, long) -> None:
    # get sign of gradient
    print(f"Fetching measure levels for station {station.name} at {station.town} measuring {station.river} ...")
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(long))
    if dates == [] or levels == []:
        return (None, None, None)

    print(f"Obtaining linear fit for data for station {station.name} ...")
    poly_l, _ = get_water_level_fit(dates, levels, 1)
    coeff_l = poly_l.coefficients[0]

    timescale_factor = round(len(dates)/(long/short))
    poly_s, _ = get_water_level_fit(dates[:timescale_factor], levels[:timescale_factor], 1)
    coeff_s = poly_s.coefficients[0]

    return (np.sign(coeff_l if abs(coeff_l) > 0.05 else 0), coeff_l, 
            np.sign(coeff_s if abs(coeff_s) > 0.05 else 0))

def evaluate_flooding(station) -> tuple[float, str]:
    # 
    frwl_short, frwl_long_mag, frwl_long = forecast_water_level_sign(station, 0.5, 30)
    rwl = station.relative_water_level()

    if any([q == None for q in (frwl_short, frwl_long, rwl)]):
        print(f'[{station.name.upper()}] Incomplete information for this station')
        return (None, None)
    
    # calibration factors
    rwl_factor = 0.04
    rwl_augment = 0.36

    short_grad_factor = 0.05 + (0.3 if rwl > 1 else 0)
    print(frwl_long_mag)
    long_grad_factor = abs(frwl_long_mag)*0.1

    # score evaluation
    score = ( ((rwl-0.8) * (rwl_factor + (rwl_augment if rwl > 1 else 0))) + 
                ((frwl_short + (0.70 if rwl > 1.2 else 0)) * short_grad_factor) + 
                (frwl_long-0.5) * long_grad_factor)

    print(f'[{station.name.upper()}] short term water level: {'rising' if frwl_short > 0 else 'falling' if frwl_short < 0 else 'steady'}')
    print(f'[{station.name.upper()}]  long term water level: {'rising' if frwl_long > 0 else 'falling' if frwl_long < 0 else 'steady'}')
    print(f'[{station.name.upper()}] water level {rwl*100}% of nominal range')

    print(f'[{station.name.upper()}] nominal range of levels: {station.typical_range}')
    print(f'[{station.name.upper()}] measured water level: {station.latest_level}')

    status = 'LOW/NONE' if score < 0.05 else \
            'MODERATE' if 0.05 <= score < 0.20 else \
            'HIGH' if 0.20 <= score < 0.50 else \
            'SEVERE'

    return score, status

def test_main() -> None:
    stations = init()
    print("initial setup complete")

    warning_stations = [station_data[0] for station_data in stations_level_over_threshold(stations, 0.3)]
    # print(f'Testing {len(warning_stations)} higher-risk stations ...\n\n')

    risk_stations = [station_data[0] for station_data in stations_highest_rel_level(stations, 75)[50:]]
    risk_towns = []

    for station in risk_stations: # stations[340:355]:
        if station.name != 'Trowlock Island':
            continue

        score, status = evaluate_flooding(station)

        risk_towns.append((station.town, status))
        
        # report
        print(f'[{station.name.upper()}]\'s flood score: {None if score is None else score*100}')
        print(f'[{station.name.upper()}] flood status: {status}\n')

    pprint(risk_towns)

if __name__ == '__main__':
    test_main()