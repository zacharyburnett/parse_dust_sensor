from io import StringIO
from os import PathLike
from types import Union

from pandas import DataFrame


class Measurement:
    def __init__(self):
        pass


class PM25AirQualityMeasurement(Measurement):
    @classmethod
    def from_pm25_air_quality(cls, text: Union[PathLike, StringIO]):
        pass


if __name__ == '__main__':
    output = DataFrame()

    print('done')
