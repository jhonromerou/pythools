class TestApi:
    def __init__(self, response):
        self.__response = response
        self.__test = []
        self.__current_index = -1

    @staticmethod
    def builder(response):
        return TestApi(response)

    def display_name(self, name: str):
        self.__current_index += 1
        self.__test.append({'name': name, 'tests': []})

        return self

    def __set_test_result(self, result):
        self.__test[self.__current_index]['tests'].append(result)
        return self

    def status_code(self, expected: int):
        current_value = self.__response.status_code
        if expected == current_value:
            self.__set_test_result({'status': 'success', 'field': 'status_code', 'expected': expected})
        else:
            self.__set_test_result({'status': 'fail', 'field': 'status_code', 'expected': expected, 'actual': current_value})

        return self

    def response(self, expected):
        current_value = self.__response.text
        if expected == current_value:
            self.__set_test_result({'status': 'success', 'field': 'response_text', 'expected': expected})
        else:
            self.__set_test_result({'status': 'fail', 'field': 'response_text', 'expected': expected, 'actual': current_value})

        return self

    def json_match(self, key: str, expected):
        current_json = self.__response.json()
        sep = key.split('.')
        for part in sep:
            if not isinstance(current_json, list):
                current_json = current_json[part]
            else:
                if len(current_json) == 0:
                    current_json = '__EMPTY_LIST__'
                    break
                current_json = current_json[int(part)]

        self.comparators(expected, current_json, key)

        return self

    def comparators(self, expected, actual, key):
        if '$' == str(expected)[0]:
            if '$is_number' == expected and isinstance(actual, int):
                self.__set_test_result({'status': 'success', 'field': key, 'expected': '{} => {}'.format(expected[1:], actual)})
            elif '$is_string' == expected and isinstance(actual, str):
                self.__set_test_result({'status': 'success', 'field': key, 'expected': expected[1:] + ' => ' + actual})
            else:
                self.__set_test_result({'status': 'fail', 'field': key, 'expected': expected, 'actual': actual})
        else:
            if expected == actual:
                self.__set_test_result({'status': 'success', 'field': key, 'expected': expected})
            else:
                self.__set_test_result({'status': 'fail', 'field': key, 'expected': expected, 'actual': actual})

    def get_result(self):
        return self.__test
