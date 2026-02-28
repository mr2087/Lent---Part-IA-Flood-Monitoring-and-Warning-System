
class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        # Return False if the data is unavailable
        if self.typical_range is None:
            return False
        
        low, high = self.typical_range

        # Return False if either data for high or low typical range is unavailable
        if low is None or high is None:
            return False
        
        # Return False if low typical range is higher than high typical range
        if low > high:
            return False
        
        return True
    
    def relative_water_level(self):
        # Return none if no latest level recorded
        if self.latest_level is None:
            return None
        # Return none if the typical range is inconsistent
        if not self.typical_range_consistent():
            return None
        
        low, high = self.typical_range
        
        return (self.latest_level - low) / (high - low)
    
def inconsistent_typical_range_stations(
    stations: list[MonitoringStation]):
    result = []

    # Loop through every MonitoringStation object in the input list
    for station in stations:
        if not station.typical_range_consistent():
            result.append(station)

    return result
