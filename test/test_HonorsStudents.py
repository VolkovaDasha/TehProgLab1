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

    def test_init_honors_students(self,
                                  input_data: tuple[DataType, int]) -> None:
        honors_students = HonorsStudents(input_data[0])
        # обращение к self.data из класса HonorsStudents (через объект honors_students)
        assert input_data[0] == honors_students.data

    def test_relevant(self, input_data: tuple[DataType, int]) -> None:
        rel = HonorsStudents(input_data[0]).rel()
        assert rel == input_data[1]
