from Types import DataType

HonorsType = dict[str, float]


class HonorsStudents:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.honors: HonorsType = {}
        self.relevant: int = 0

    def rel(self) -> HonorsType:
        for key in self.data:
            x = 0
            self.honors[key] = 0.0
            for subject in self.data[key]:
                if subject[1] >= 90:
                    x += 1
            if x == len(self.data[key]):
                self.relevant += 1
        return self.relevant
