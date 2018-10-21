import os
from collections import namedtuple
import csv

Record = namedtuple(
    'Record',
    'id,awareness,interested,Algeria,Argentina,Australia,Belgium,Bosnia_Herzegovina,Brazil,Cameroon,Chile,Colombia,'
    'Costa_Rica,Croatia,Ecuador,England,France,Germany,Ghana,Greece,Honduras,Iran,Italy,Ivory_Coast,Japan,Mexico,'
    'Netherlands,Nigeria,Portugal,Russia,South_Korea,Spain,Switzerland,United_States,Uruguay,China,India,Thailand,'
    'Turkey,Cuba,Ethiopia,Vietnam,Ireland,Gender,Age,Household_Income,Education,Location'
)

class FoodResearcher:
    def __init__(self):
        self.__data = []
        self.__load_file()
        # self.__load_transpose_file()

    def __load_file(self):
        directory = os.path.dirname(__file__)
        data_file = os.path.join(directory,'food-world-cup-data.csv')

        with open(data_file) as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.__data.append(self.__parse_row(row))

    def __load_transpose_file(self):
        directory = os.path.dirname(__file__)
        data_file = os.path.join(directory,'food-world-cup-data.csv')
        self.__transpose_data = []
        reader = zip(*csv.reader(open(data_file, "r")))

        for row in reader:
            print(row)

    def __parse_entry(self, row, entry):
        try:
            row[entry] = int(row[entry])
        except ValueError:
            row[entry] = 0

    def __parse_row(self, row):
        self.__parse_entry(row, 'Algeria')
        self.__parse_entry(row, 'Argentina')
        self.__parse_entry(row, 'Australia')
        self.__parse_entry(row, 'Belgium')
        self.__parse_entry(row, 'Bosnia_Herzegovina')
        self.__parse_entry(row, 'Brazil')
        self.__parse_entry(row, 'Cameroon')
        self.__parse_entry(row, 'Chile')
        self.__parse_entry(row, 'Colombia')
        self.__parse_entry(row, 'Costa_Rica')
        self.__parse_entry(row, 'Croatia')
        self.__parse_entry(row, 'Ecuador')
        self.__parse_entry(row, 'England')
        self.__parse_entry(row, 'France')
        self.__parse_entry(row, 'Germany')
        self.__parse_entry(row, 'Ghana')
        self.__parse_entry(row, 'Greece')
        self.__parse_entry(row, 'Honduras')
        self.__parse_entry(row, 'Iran')
        self.__parse_entry(row, 'Italy')
        self.__parse_entry(row, 'Ivory_Coast')
        self.__parse_entry(row, 'Japan')
        self.__parse_entry(row, 'Mexico')
        self.__parse_entry(row, 'Netherlands')
        self.__parse_entry(row, 'Nigeria')
        self.__parse_entry(row, 'Portugal')
        self.__parse_entry(row, 'Russia')
        self.__parse_entry(row, 'South_Korea')
        self.__parse_entry(row, 'Switzerland')
        self.__parse_entry(row, 'Spain')
        self.__parse_entry(row, 'United_States')
        self.__parse_entry(row, 'Uruguay')
        self.__parse_entry(row, 'China')
        self.__parse_entry(row, 'India')
        self.__parse_entry(row, 'Thailand')
        self.__parse_entry(row, 'Turkey')
        self.__parse_entry(row, 'Cuba')
        self.__parse_entry(row, 'Ethiopia')
        self.__parse_entry(row, 'Vietnam')
        self.__parse_entry(row, 'Ireland')


        record = Record( **row )
        return record

    def get_average(self):
        return sorted(self.__data, key=lambda r: r.Algeria, reverse=True)
