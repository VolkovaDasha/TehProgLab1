from Types import DataType

RatingType = dict[str, float]


class CalcRating:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data  # students
        self.rating: RatingType = {}  # пустой словарь

    def calc(self) -> RatingType:
        for key in self.data:
            self.rating[key] = 0.0  # rating[key] - это доступ к значению
            for subject in self.data[key]:  # перебираем кортеж
                self.rating[key] += subject[1]
            self.rating[key] /= len(self.data[key])
        return self.rating
