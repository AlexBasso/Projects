import requests
from typing import Dict, Any


def _make_response(method: str, url: str, headers: Dict, params: Dict,
                   timeout: int, success=200) -> Any:
    """
    Private function that makes a request and checks status code. In case status code is 200(success) return response,
    otherwise return error status code.

    :param method: Method for requesting from url.
    :param url: url from which something is requested.
    :param headers: required token and site url.
    :param params: params that api needs to process request.
    :param timeout: timeout
    :param success: default status code of request.
    :return: in case status code is 200(success) return response, otherwise return error status code.
    """

    response = requests.request(
        method,
        url,
        headers=headers,
        params=params,
        timeout=timeout
    )
    status_code = response.status_code
    if status_code == success:
        return response

    return status_code


def _get_weather_data(method: str, url: str, headers: Dict, params: Dict,
                      timeout: int, func=_make_response):
    """
    Private function that executes the function that will make request(_make_response). This step make little sense
    when there is only one request function(_make_response), however would be very helpful, if in the future
    there will be more request functions.

    :param method: Method for requesting from url.
    :param url: url from which something is requested.
    :param headers: required token and site url.
    :param params: params that api needs to process request.
    :param timeout: timeout
    :param func: _make_response
    :return: func
    """
    response = func(method, url, headers=headers, params=params, timeout=timeout)

    return response


class SiteApiInterface:
    """
    Base class interface for accessing private function for requesting weather data.
    """

    @classmethod
    def get_weather(cls):
        """
        @classmethod of SiteApiInterface for requesting weather data.
        :return: private function for requesting weather data
        """
        return _get_weather_data


if __name__ == '__main__':
    SiteApiInterface()
