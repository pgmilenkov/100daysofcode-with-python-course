import os
import csv
from collections import namedtuple
from typing import List

Record = namedtuple(
    'Record',
    'state,drivers_fatal_collisions,drivers_speeding,drivers_alcohol_impaired,'
    'drivers_not_distracted,drivers_first_collision,car_insurance,insurance_company_losses'
)

class BadDriversResearch:

    def __init__(self):
        self.__data = []
        self.__load_file()

    def __load_file(self):
        base_folder = os.path.dirname(__file__)
        data_file = os.path.join(base_folder, 'bad-drivers.csv')

        with open(data_file) as f:
            reader = csv.DictReader(f)

            for row in reader:
                record = self.__parse_row(row)
                self.__data.append(record)

    def __parse_row(self, row):
        row['drivers_fatal_collisions'] = float(row['drivers_fatal_collisions'])
        row['drivers_speeding'] = int(row['drivers_speeding'])
        row['drivers_alcohol_impaired'] = float(row['drivers_alcohol_impaired'])
        row['drivers_not_distracted'] = float(row['drivers_not_distracted'])
        row['drivers_first_collision'] = float(row['drivers_first_collision'])
        row['car_insurance'] = float(row['car_insurance'])
        row['insurance_company_losses'] = float(row['insurance_company_losses'])

        record = Record( **row )
        return record

    def sort_states_by_died_drivers(self) -> List[Record]:
        return sorted(self.__data, key=lambda r: r.drivers_fatal_collisions, reverse=True)

    def sort_states_by_speed(self) -> List[Record]:
        return sorted(self.__data, key=lambda r: r.drivers_speeding, reverse=True)

    def sort_states_by_alcohol(self) -> List[Record]:
        return sorted(self.__data, key=lambda r: r.drivers_alcohol_impaired, reverse=True)

    def sort_states_by_insurance_company_loss(self) -> List[Record]:
        return sorted(self.__data, key=lambda r: r.insurance_company_losses, reverse=True)

    def sort_states_by_alcohol(self) -> List[Record]:
        return sorted(self.__data, key=lambda r: r.drivers_alcohol_impaired, reverse=True)
