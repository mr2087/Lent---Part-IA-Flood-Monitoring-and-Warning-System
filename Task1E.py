
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number, _get_distance

def main():
    # build main station list
    stations : list = build_station_list(use_cache = True)

    # first test: N = 9
    rivers_with_stations : list = rivers_by_station_number(stations, N=17)

    print(" ======= [TASK 1E: Representative Output] ======= ")
    print(rivers_with_stations)
    print(print(_get_distance((90, 0), (-90, 0))))

def test_1E1() -> None:
    """Testing function. Check if """

    # using representative (cached) output
    stations : list = build_station_list(use_cache = True)

    rivers_with_stations : list = rivers_by_station_number(stations, N = 9)

    # preliminary check
    assert len(rivers_with_stations) >= 9
    
def test1E2() -> None:
    """Second testing function. Check what happens if """

if __name__ == '__main__':
    main()