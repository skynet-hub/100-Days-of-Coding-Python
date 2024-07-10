#learning to master dictionaries and lists(nesting)


travel_log = [

    {
        "country": "France",
        "Cities_visited": ["Paris", "Lille", "Dijon"],
        "Total_visits": 12
    },

    {
        "country": "Germany",
        "Cities_visited": ["berlin", "Humburg", "Stuttgart"],
        "tatal_visits": 5
    }
]

def add_new_country(country, cities_visited, total_visits):
    new_dict = {}
    new_dict["country"] = country
    new_dict["cities_visited"] = cities_visited
    new_dict["total_visits"] = total_visits

    travel_log.append(new_dict)

add_new_country("Russia", ["Moscow", "Saint_paris"], 2)
print(travel_log)