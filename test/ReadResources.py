class ReadResources:
    @staticmethod
    def get_path(file_path: str):
        return '../resources/{}'.format(file_path)

    @staticmethod
    def get_content(file_path: str):
        file = open(ReadResources.get_path(file_path), "r")
        content = file.read()
        file.close()

        return content
