import pytest
from linkermc import portal
from linkermc.dimension import Dimension

def test_overworld_to_nether():
    p_main = portal.Portal(Dimension.overworld, coords=(0,0,0), extent=(0,0))
    # good match
    p_perfect_match = portal.Portal(Dimension.nether, coords=(0,0,0), extent=(0,0))
    assert p_main.links_to(p_perfect_match)
    # limit in X
    p_limit_x = portal.Portal(Dimension.nether, coords=(16,0,0), extent=(0,0))
    assert p_main.links_to(p_limit_x)
    # high Y
    p_high_y = portal.Portal(Dimension.nether, coords=(16,255,0), extent=(0,0))
    assert p_main.links_to(p_high_y)
    # out_of_range
    p_high_y = portal.Portal(Dimension.nether, coords=(17,255,0), extent=(0,0))
    assert not p_main.links_to(p_high_y)
