import os


class FileSelection:
    def __init__(self):
        self.__extensions = []

    @staticmethod
    def from_dir(baseDir: str, extensions: list):
        i = 0
        options = []
        for path in os.listdir(baseDir):
            if extensions is not None:
                topDir = os.path.join(baseDir, path)
                is_dir = os.path.isdir(topDir)
                if is_dir:
                    print('  {} 📁 {} '.format(i, path))
                    options.append({'path': topDir, 'is_dir': is_dir})
                    i = i + 1
                else:
                    for ext in extensions:
                        if path.endswith('.' + ext):
                            print('  {} 📋 {} '.format(i, path))
                            options.append({'path': topDir, 'is_dir': is_dir})
                            i = i + 1

        option = int(input("select option: "))

        selected_option = options[option]
        if selected_option['is_dir']:
            print("select option from " + selected_option['path'])
            return FileSelection.from_dir(selected_option['path'], extensions)

        return selected_option['path']
