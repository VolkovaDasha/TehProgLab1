from Types import DataType
from DataReader import DataReader
import yaml
from yaml.loader import SafeLoader


class YamlTextDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            # читаем документ и преобразуем в словарь, указываем загрузчик
            data = yaml.load(file, Loader=yaml.SafeLoader)
            for people in data:
                # получаем список пар (ключ, значение), содержащихся в словаре.
                for name, subjects in people.items():
                    self.key = name
                    # создаем пустой список с ключом кеу в словаре students
                    self.students[self.key] = []
                    for subject, rating in subjects.items():
                        # добавляем кортеж в список с ключом name
                        self.students[name].append((subject, int(rating)))
        return self.students
