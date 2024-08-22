import re

import yaml


class FReader:
    @staticmethod
    def tsv(file_path: str, columns_name: list, start_line=1, end_line=1000000):
        return FReader.with_delimiter('\t', file_path, columns_name, start_line, end_line)

    @staticmethod
    def csv(file_path: str, columns_name: list, start_line=1, end_line=1000000):
        return FReader.with_delimiter(',', file_path, columns_name, start_line, end_line)

    @staticmethod
    def yaml(yml_path: str, envs: dict):
        with open(yml_path, 'r') as file:
            content = file.read().strip()
            matched = re.findall(r'\$\{(.*)}', content)
            for key in matched:
                env = envs[key]
                if env is not None:
                    content = content.replace('${' + key + '}', env)
            return yaml.safe_load(content)

    @staticmethod
    def with_delimiter(delimiter: str, file_path: str, columns_name: list, start_line=1, end_line=1000000):
        data = []
        line_reads = 0
        start_line = start_line - 1
        end_line = end_line - 1
        with open(file_path, 'r') as file:
            for line in file.readlines():
                if not start_line > line_reads:
                    content = line.strip().split(delimiter)
                    data_line = {}
                    index = 0
                    for field in columns_name:
                        data_line[field] = content[index]
                        index += 1
                    data.append(data_line)
                line_reads += 1
                if line_reads > end_line:
                    return data

        return data
