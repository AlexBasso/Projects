import datetime
from typing import List, Dict, Optional, Any

from tg_api.core import get_weather_via_api


def format_weather_response(weather_data_hour: Dict, state: Optional[Any] = False) -> List:
    """
    Basic function that formats data from api list in a readable for final response.

    :param weather_data_hour:  hourly data dict.
    :param state: bool that checks if an additional param needs to be added to the return list.
    :return: List
    """
    weather_response = []
    weather_response.extend(['Date: ' + weather_data_hour["datetimeStr"][0:13].replace("T", " ") + ':00',
                             'Temperature: ' + str(weather_data_hour["temp"]) + ' C',
                             'Humidity: ' + str(weather_data_hour["humidity"]),
                             'Clouds: ' + weather_data_hour["conditions"],
                             'Wind speed: ' + str(weather_data_hour["wspd"]) + ' km/h'])

    if state:
        weather_response.append(weather_data_hour["temp"])

    return weather_response


def non_nested_weather_response(weather_nested_list: List) -> List:
    """
    Basic function that turns a neste list of data in to a non-nested list.

    :param weather_nested_list: data about weather form api in list form
    :return: List
    """
    non_nested_response = []
    for weather_hourly_list in weather_nested_list:
        temp_var = '\n'.join(weather_hourly_list) + '\n'
        non_nested_response.append(temp_var)
    return non_nested_response


def now_weather_req(weather_data_by_hour_list: List) -> List:
    """
    Basic function that formats (Date, Temperature, Humidity, Clouds, Wind speed) and returns weather info for current
    hour, found in the hourly data list.

    :param weather_data_by_hour_list:  hourly data list in which the right hour is found for the response.
    :return: List
    """
    weather_response = []
    date_time_str = datetime.datetime.now().strftime("%Y-%m-%dT%H")
    for weather_data_hour in weather_data_by_hour_list:
        if weather_data_hour["datetimeStr"][0:13] == date_time_str:
            weather_response = format_weather_response(weather_data_hour)
            break
    return weather_response


def min_max_weather_req(type_func: str, weather_data_by_hour_list: List) -> List:
    """
    Basic function that formats (Date, Temperature, Humidity, Clouds, Wind speed) and returns weather info for minimal
    or maximal Temperature in a given day, searches by hour found in the hourly data list.

    :param type_func: "min" or "max" - by use of 'eval' determines what method to run.
    :param weather_data_by_hour_list: hourly data list in which the right hour is found for the response.
    :return: List
    """
    weather_response = []
    date_time_str = datetime.datetime.now().strftime("%Y-%m-%d")
    for weather_data_hour in weather_data_by_hour_list:
        hourly_weather_response = []

        if weather_data_hour["datetimeStr"][0:10] == date_time_str:
            hourly_weather_response = format_weather_response(weather_data_hour, state=True)

        if hourly_weather_response:
            weather_response.append(hourly_weather_response)

    min_max_weather_response = eval(type_func)(weather_response, key=lambda k: k[5])
    min_max_weather_response.pop()

    return min_max_weather_response


def custom_weather_req(data_time: str, weather_data_by_hour_list: List) -> List:
    """
    Basic function that formats (Date, Temperature, Humidity, Clouds, Wind speed) and returns weather info for specified
    City and day/hour, searches by hour found in the hourly data list.

    :param data_time: specified day/hour
    :param weather_data_by_hour_list: hourly data list in which the right hour is found for the response.
    :return: List
    """

    try:
        datetime.datetime.fromisoformat(data_time).strftime("%Y-%m-%dT%H")
        data_time_test = data_time.replace('T', ' ')
        date_object = datetime.datetime.strptime(data_time_test, '%Y-%m-%d %H')
    except BaseException:
        return [f'Incorrect format, please try again using:', 'CITY_NAME YYYY-MM-DD HH']

    max_forcast_date = datetime.datetime.now() + datetime.timedelta(days=7)

    if max_forcast_date < date_object:
        return ['Incorrect date - forecasts are only made for 7 days.', 'Please try again with a different date.']

    weather_response = []
    for weather_data_hour in weather_data_by_hour_list:
        hourly_weather_response = []

        if weather_data_hour["datetimeStr"][0:13] == data_time:
            hourly_weather_response = format_weather_response(weather_data_hour)

        if hourly_weather_response:
            weather_response.append(hourly_weather_response)

    return non_nested_weather_response(weather_response)


def weather_req(argument: str, command: str) -> List:
    """
    Function that returns list of weather data in response to the request. Separates City name from date and based on
    command returns a list of requested info.

    :param argument: arguments that come after command /"command args"
    :param command: actual command /'command'
    :return: List of requested info
    """
    temp_list = argument.split()
    city = temp_list.pop(0)
    data_time = 'T'.join(temp_list)

    weather_data_by_hour_list = get_weather_via_api(city=city)["locations"][city]["values"]

    match command:
        case 'now':
            response = now_weather_req(weather_data_by_hour_list)
        case 'low':
            response = min_max_weather_req('min', weather_data_by_hour_list)
        case 'high':
            response = min_max_weather_req('max', weather_data_by_hour_list)
        case "custom":
            response = custom_weather_req(data_time, weather_data_by_hour_list)

    return response
