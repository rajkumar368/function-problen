def city_with_states(Input_dict):
    cities_list = []
    city_state_dict = {}
    for value in Input_dict.values():
        city_list = cities_list.extend(value)
    cites = set(cities_list)
    
    for city in cites:
        city_state_dict[city] = [key for key,value in Input_dict.items() if city in value ]
    return city_state_dict