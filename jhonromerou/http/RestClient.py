import requests


class RestClient:
    def __init__(self):
        self.__method = 'GET'
        self.__url = ''
        self.__headers = {}
        self.__query_params = {}
        self.__data = ''

    @staticmethod
    def builder():
        return RestClient()

    def url(self, path: str):
        """Sets url to request. if `path` is defined append to url request"""
        self.__url = '{0}{1}'.format(self.__url, path)

        return self

    def get(self, url: str):
        self.__method = 'GET'
        self.__url = url
        return self

    def put(self, url: str):
        self.__method = 'PUT'
        self.__url = url
        return self

    def post(self, url: str):
        self.__method = 'POST'
        self.__url = url
        return self

    def headers(self, values: dict):
        """Sets headers to request. if some `key` exists then replace.
        
        example: values = {header1: value1, header2: value2}"""
        if values is not None:
            for key, value in values.items():
                self.__headers[key] = value
        return self

    def data(self, data: str):
        self.__data = data
        return self

    def query_params(self, params: dict):
        self.__query_params = {}
        for key, value in params.items():
            self.__query_params[key] = value
        return self

    def get_response(self, view_url=False):
        """Call a request with defined properties
        
        return `<response> Requests.Response`"""
        if view_url:
            print('\n' + self.get_url_request())
        return self.__make_request()

    def __make_request(self):
        params = ''
        for key in self.__query_params:
            params += '{}={}&'.format(key, self.__query_params[key])

        url = '{}?{}'.format(self.__url, params) if params != '' else self.__url

        if self.__method == 'GET':
            return requests.get(url, data=self.__data, headers=self.__headers)

        if self.__method == 'POST':
            return requests.post(url, data=self.__data, headers=self.__headers)
        if self.__method == 'PUT':
            return requests.put(url, data=self.__data, headers=self.__headers)

    def get_url_request(self):
        return '{0} {1}'.format(self.__method, self.__url)
