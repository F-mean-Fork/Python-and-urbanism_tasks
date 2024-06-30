def get_count_city_mentions(cities, target_city):
    target_city_lower = target_city.lower()
    count = 0
    for city in cities:
        if city.lower() == target_city_lower:
            count += 1
    return count

if __name__ == "__main__":
    cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "САНКТ-ПЕТЕРБУРГ"]
    target = "Санкт-Петербург"
    mentions = get_count_city_mentions(cities, target)  # TODO Посчитайте количество упоминаний
    print(f"Количество упоминаний города '{target}' равно {mentions}")
