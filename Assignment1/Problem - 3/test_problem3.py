import pytest
from solution3 import city_with_states

def test_city_with_states():
    Input_dict = {'New Hampshire':['Concord', 'Hanover'],'Massachusetts':['Boston','Concord','Springfield'],                           'Illinois': ['Chicago', 'Springfield', 'Peoria']}
    assert city_with_states(Input_dict) ==  {'Hanover': ['New Hampshire'],'Chicago': ['Illinois'],
                                             'Boston':['Massachusetts'],'Peoria': ['Illinois'],                                                                  'Concord': ['New Hampshire','Massachusetts'],                                                                        'Springfield': ['Massachusetts', 'Illinois'] }
    
    
def test_city_with_states2():
    Input_dict = {'Massachusetts':['Boston','Concord','Springfield'],'Illinois': ['Chicago', 'Springfield', 'Peoria']}
    assert city_with_states(Input_dict) ==  {'Chicago': ['Illinois'],
                                             'Boston':['Massachusetts'],'Peoria': ['Illinois'],                                                                  'Concord': ['Massachusetts'],                                                                                        'Springfield': ['Massachusetts', 'Illinois'] }