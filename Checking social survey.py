def get_common_cities(group1, group2):
    group3 = list(set(group1) & set(group2))
    group3.sort()
    return group3


if __name__ == "__main__":
    group1 = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург"]
    group2 = ["Санкт-Петербург", "Екатеринбург", "Казань", "Сочи"]

    cities = get_common_cities(group1, group2)
    print(cities)  # ['Екатеринбург', 'Санкт-Петербург']
