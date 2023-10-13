import argparse
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from HonorsStudents import HonorsStudents
from YamlTextDataReader import YamlTextDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str,
                        required=True, help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    vpath = path.split(".")
    if vpath[-1] == "txt":
        reader = TextDataReader()
        students = reader.read(path)
        print("Students: ", students)
        rating = CalcRating(students).calc()
        print("Rating: ", rating)
    else:
        reader = YamlTextDataReader()
        students = reader.read(path)
        print("Students: ", students)
        honor = HonorsStudents(students).rel()
        print("Количество студентов отличников =", honor)



if __name__ == "__main__":
    main()
