# TODO написать функцию filter_city_by_population

def filter_city_by_population(city_list_with_population, threshold=1000000):
    new_list = [city for city in city_list_with_population if city["population"] > threshold]
    return new_list
if __name__ == "__main__":
    city_list_with_population = [
        {"city": "Москва", "population": 12500000},
        {"city": "Санкт-Петербург", "population": 5400000},
        {"city": "Екатеринбург", "population": 1500000},
        {"city": "Нижний Новгород", "population": 1300000},
        {"city": "Ижевск", "population": 600000},
    ]

    print(filter_city_by_population(city_list_with_population))
