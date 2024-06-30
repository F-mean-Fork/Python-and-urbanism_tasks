def get_capitalize_city_names(list_):
    res = [s.capitalize() for s in list_]
    return res

if __name__ == "__main__":
    city_list = ["москва", "иЖЕВСк", "Владивосток", "новосибирсК", "мУРМАНСК"]
    new_city_list = get_capitalize_city_names(city_list)

    print(new_city_list)  # ['Москва', 'Ижевск', 'Владивосток', 'Новосибирск', 'Мурманск']
