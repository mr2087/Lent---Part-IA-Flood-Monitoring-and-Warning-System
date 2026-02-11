import pytest

from math import pi

# functions to be tested
from floodsystem.geo import _hav, _get_distance 

# miscellaneous tests
def test_1X1() -> None:
    assert _hav(0.2)  == pytest.approx(0.00996671107)
    assert _hav(pi)   == pytest.approx(1.0)
    assert _hav(2*pi) == pytest.approx(0)

def test_1X2() -> None:
    assert _get_distance((50.110924, 8.682127), # Frankfurt
                         (48.864716, 2.349014)  # Paris
                        ) == pytest.approx(477815.9)
    
    _get_distance((90, 0), (-90, 0))            # check for edge case, latitude
