def classify_urban_block(square):
    if square > 0 and square < 1000:
        return "Жилой"
    elif square >= 1000 and square < 5000:
        return "Коммерческий"
    elif square >= 5000 and square < 15000:
        return "Промышленный"
    elif square >= 15000:
        return "Неизвестный тип блока"
    else:
        return "Некорректное значение площади блока"


if __name__ == '__main__':
    print(classify_urban_block(500))  # Жилой
    print(classify_urban_block(1000))  # Коммерческий
    print(classify_urban_block(7000))  # Промышленный
