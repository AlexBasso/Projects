import json
from typing import Dict

from config_data.config import SiteSettings
from handlers.custom_handlers.site_api_handler import SiteApiInterface

tg_settings = SiteSettings()
site_api = SiteApiInterface()

weather = site_api.get_weather()

url = tg_settings.host_url

headers = {
    "X-RapidAPI-Key": tg_settings.site_api.get_secret_value(),
    "X-RapidAPI-Host": tg_settings.host_api
}


def get_weather_via_api(city: str) -> Dict:
    """
    Functon that gathers all needed data in order to make a request to api and sends it to the actual function that
    will make the request.
    :param city: specifies the city for which to return weather info
    :return: weather data about specified city in Dict form.
    """
    querystring = {"aggregateHours": "1", "location": city, "contentType": "json",
                   "unitGroup": "metric", "shortColumnNames": "false"}

    response = weather('GET', url, headers=headers, params=querystring, timeout=5)
    data = json.loads(response.text)

    return data
