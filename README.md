# Лабораторная 1 по дисциплине "Технологии программирования"
Знакомство с системой контроля версий Git и инструментом CI/CD GitHub Actions
Цели работы:
1. Познакомиться c распределенной системой контроля версий кода Git и ее функциями;
2. Познакомиться с понятиями «непрерывная интеграция» (CI) и «непрерывное развертывание» 
(CD), определить их место в современной разработке программного обеспечения;
3. Получить навыки разработки ООП-программ и написания модульных тестов к ним на 
современных языках программирования;
4. Получить навыки работы с системой Git для хранения и управления версиями ПО;
5. Получить навыки управления автоматизированным тестированием программного обеспечения, 
расположенного в системе Git, с помощью инструмента GitHub Actions

Проверим работоспособность первоначальной программы. Создадим виртуальное окружение и запустим необходимые пакеты после чего проверим программу на работоспособность:

![image](https://github.com/VolkovaDasha/TehProgLab1/assets/118906106/570ceb5d-9f85-466c-ab0e-60ac515f2b7d)
![image](https://github.com/VolkovaDasha/TehProgLab1/assets/118906106/9ced85a8-ab66-432c-b80c-c7825d2233db)
![image](https://github.com/VolkovaDasha/TehProgLab1/assets/118906106/f7077247-ac5b-4c8e-be06-f2db419d20d9)

## Индивидуальное задание: 
![image](https://github.com/VolkovaDasha/TehProgLab1/assets/118906106/d39fb935-82bc-40a4-b6cb-854e0f6c7c59)


#### Создадим наследника класса DataReader, который обрабатывает входной файл data.yaml. 

Для этого установим библиотеку YAML в Python – через диспетчер пакетов pip, затем импортируем пакет yaml и для функции yaml.load() укажем загрузчик SafeLoader.

```python
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
            data = yaml.load(file, Loader=yaml.FullLoader)
            for people in data:
               for name, subjects in people.items():
                self.key = name
                self.students[self.key] = []
                for subject, rating in subjects.items():
                    self.students[name].append((subject, int(rating)))  
        return self.students
```
Проверим работу программы, после внесения изменений в main.py:
![image](https://github.com/VolkovaDasha/TehProgLab1/assets/118906106/6659712a-01be-49c5-86db-ea631f350ce6)

#### Создадим модульный тест:

```python

import pytest
from src.Types import DataType
from src.YamlTextDataReader import YamlTextDataReader

class TestYamlDataReader:
    
    @pytest.fixture() #подготовка контекста для выполнения тестов
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = "---\n" +\
            "- Иванов Константин Дмитриевич:\n" + \
            "    математика: 91\n" + \
            "    химия: 100\n" + \
            "- Петров Петр Семенович:\n" + \
            "    русский язык: 87\n" + \
            "    литература: 78\n"
        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return text, data
    @pytest.fixture()
    def filepath_and_data(self,file_and_data_content: tuple[str, DataType],tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.yaml")  #создаем временную папку.пустой каталог и добавление имени нового файла 
        p.write_text(file_and_data_content[0], encoding='utf-8')  #записываем путь
        return str(p), file_and_data_content[1]        # путь и data
    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = YamlTextDataReader().read(filepath_and_data[0])  #(ссылка путь p)
        assert file_content == filepath_and_data[1]
```

#### Проверим работу теста:

![image](https://github.com/VolkovaDasha/TehProgLab1/assets/118906106/b8f52839-ba29-4f36-8f11-c75834eb06d2)


#### Создадим класс, реализующий расчет количества студентов-отличников.

```python
from Types import DataType

HonorsType = dict[str, float]


class HonorsStudents:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data 
        self.honors: HonorsType = {}
        self.relevant: int = 0
       

    def rel(self) -> HonorsType:
        for key in self.data:
            x=0
            self.honors[key] = 0.0
            for subject in self.data[key]:
                if subject[1] >= 90:
                   x += 1
            if x == len(self.data[key]):
               self.relevant +=1
        return self.relevant
```
#### Внесем соответствующие изменения в main.py:

```python
import argparse
import sys

from CalcRating import CalcRating
# from TextDataReader import TextDataReader
from HonorsStudents import HonorsStudents
from YamlTextDataReader import YamlTextDataReader
 

def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,help="Path to datafile")
    args = parser.parse_args(args)
    return args.path
def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = YamlTextDataReader()
    students = reader.read(path)
    print("Students: ", students)
    # rating = CalcRating(students).calc()
    # print("Rating: ", rating)
    honor = HonorsStudents(students).rel()
    print ("Количество студентов отличников =", honor)

if __name__ == "__main__":
    main()

```
#### Проверим работоспособность программы:
![image](https://github.com/VolkovaDasha/TehProgLab1/assets/118906106/d9ae0df4-67a3-457e-9daa-57e8e7a3ef11)

#### Создадим модульный тест:
```python
from src.Types import DataType
from src.HonorsStudents import HonorsStudents
import pytest

RatingsType = dict[str, float]

class TestHonorsStudents:
    
        @pytest.fixture()
        def input_data(self) -> tuple[DataType, int]:
            data: DataType = {
                "Абрамов Петр Сергеевич":
                    [
                        ("математика", 96),
                        ("русский язык", 91),
                        ("программирование", 100)
                    ],
                "Петров Игорь Владимирович":
                    [
                        ("математика", 61),
                        ("русский язык", 80),
                        ("программирование", 78),
                        ("литература", 97)
                    ]     
            }
            relevant: int = 1

            return data, relevant
        def test_init_honors_students(self, input_data: tuple[DataType,int]) -> None:          
            honors_students = HonorsStudents(input_data[0])
            assert input_data[0] == honors_students.data # обращение к self.data из класса HonorsStudents (через объект honors_students)
        def test_relevant(self, input_data: tuple[DataType, int]) -> None:
            rel = HonorsStudents(input_data[0]).rel()
            assert rel == input_data[1]
```
#### Проверим работу теста: 

![image](https://github.com/VolkovaDasha/TehProgLab1/assets/118906106/810bfa60-6753-4f73-9fd6-21c8e3ee5fc5)


