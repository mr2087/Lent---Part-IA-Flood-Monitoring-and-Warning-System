from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

def test_stations_level_over_threshold():
    # Create test stations
    s1 = MonitoringStation("id1", "m1", "A", (0,1), (0,0), "River1", "Town1")
    s2 = MonitoringStation("id2", "m2", "B", (0,1), (0,0), "River2", "Town2")
    s3 = MonitoringStation("id3", "m3", "C", (0,1), (0,0), "River3", "Town3")

    # Give them test levels
    s1.latest_level = 0.9
    s2.latest_level = 0.5
    s3.latest_level = None

    stations = [s1, s2, s3]
    result = stations_level_over_threshold(stations, 0.8)

    assert len(result) == 1
    assert result[0][0].name == "A"
    assert result [0][1] == 0.9

def test_stations_highest_rel_level():
    # Create test stations
    s1 = MonitoringStation("id1", "m1", "A", (0,1), (0,0), "River1", "Town1")
    s2 = MonitoringStation("id2", "m2", "B", (0,1), (0,0), "River2", "Town2")
    s3 = MonitoringStation("id3", "m3", "C", (0,1), (0,0), "River3", "Town3")
    s4 = MonitoringStation("id1", "m1", "A", (0,1), (0,0), "River1", "Town1")
    s5 = MonitoringStation("id2", "m2", "B", (0,1), (0,0), "River2", "Town2")
    s6 = MonitoringStation("id3", "m3", "C", (0,1), (0,0), "River3", "Town3")
    s7 = MonitoringStation("id1", "m1", "A", (0,1), (0,0), "River1", "Town1")
    s8 = MonitoringStation("id2", "m2", "B", (0,1), (0,0), "River2", "Town2")
    s9 = MonitoringStation("id3", "m3", "C", (0,1), (0,0), "River3", "Town3")
    s10 = MonitoringStation("id1", "m1", "A", (0,1), (0,0), "River1", "Town1")
    s11 = MonitoringStation("id2", "m2", "B", (0,1), (0,0), "River2", "Town2")
    s12 = MonitoringStation("id3", "m3", "C", (0,1), (0,0), "River3", "Town3")

    # Give them test levels
    s1.latest_level = 0.9
    s2.latest_level = 0.5
    s3.latest_level = None
    s4.latest_level = 0.1
    s5.latest_level = 0.2
    s6.latest_level = 0.3
    s7.latest_level = 0.4
    s8.latest_level = 0.5
    s9.latest_level = 0.6
    s10.latest_level = 0.7
    s11.latest_level = 0.9
    s12.latest_level = 1.0

    stations = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]
    result = stations_highest_rel_level(stations, 8)

    # Get levels for testing
    levels = [level for (_, level) in result]

    assert len(result) == 8
    assert result[0][0].name == "L" #s12
    assert result [0][1] == 1.0

    expected_top_levels = sorted(
        [0.9,0.5,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        reverse=True
    )[:8]

    assert levels == expected_top_levels