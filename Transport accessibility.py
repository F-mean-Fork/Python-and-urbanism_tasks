def calculate_transport_accessibility(list_travel_times: list, extra_time=0):
    return sum(list_travel_times)/len(list_travel_times)+extra_time


if __name__ == "__main__":
    list_travel_times = [10, 15, 20, 5, 25]
    accessibility = calculate_transport_accessibility(list_travel_times)
    print(f"Среднее время доступности: {accessibility} минут")

    accessibility = calculate_transport_accessibility(list_travel_times, extra_time=5)
    print(f"Среднее время доступности: {accessibility} минут")
