import pytest
from src.Types import DataType
from src.YamlTextDataReader import YamlTextDataReader


class TestYamlDataReader:

    @pytest.fixture()  # подготовка контекста для выполнения тестов
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
    def filepath_and_data(self, file_and_data_content: tuple
                          [str, DataType], tmpdir) -> tuple[str, DataType]:
        # создаем временную папку.пустой каталог, добавление имени нового файла
        p = tmpdir.mkdir("datadir").join("my_data.yaml")
        # записываем путь
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]        # путь и data

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = YamlTextDataReader().read(
            filepath_and_data[0])  # (ссылка путь p)
        assert file_content == filepath_and_data[1]
