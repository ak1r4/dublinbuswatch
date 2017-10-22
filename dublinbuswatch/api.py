import requests


class RTPI:
    _SERVER = 'https://data.dublinked.ie/cgi-bin/rtpi'

    @classmethod
    def rt_bus_info(cls, stopid, routeid=None, maxresults=None, operator=None):
        params = {'stopid': stopid}

        if routeid:
            params.update({'routeid': routeid})

        if maxresults:
            params.update({'maxresults': maxresults})

        if operator:
            params.update({'operator': operator})

        return cls._fetch_result('/realtimebusinformation', params)

    @classmethod
    def route_info(cls, routeid, operator):
        params = {'routeid': routeid, 'operator': operator}
        return cls._fetch_result('/routeinformation', params)

    @classmethod
    def _fetch_result(cls, api_endpoint, params):
        return requests.get('{}{}'.format(cls._SERVER, api_endpoint),
                            params=params).json()
