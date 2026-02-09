
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def main():
    # build main station list
    stations : list = build_station_list(use_cache = True)

    # first test: N = 9
    rivers_with_stations : list = rivers_by_station_number(stations, N=9)

    print(" ======= [TASK 1E: Representative Output] ======= ")
    print(rivers_with_stations)

if __name__ == '__main__':
    main()