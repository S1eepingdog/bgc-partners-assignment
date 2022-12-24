import pandas as pd

from . import constants
from .utils import *


class Parser(object):
    def __init__(self, vendor_file="corp_pfd.dif", reference_field="reference_fields.csv",
                 reference_data="reference_securities.csv"):
        self.vendor_file = vendor_file
        self.reference_field = reference_field
        self.reference_data = reference_data

    def parse_vendor_data(self):
        """
        parse the data in the input file
        :return: data in dataframe from the input file
        """
        fields = self.parse_vendor_field()
        data = []
        flag = False
        for line in skip_comments(self.vendor_file):
            raw = line.decode().rstrip()
            if constants.START_OF_DATA == raw:
                flag = True
                continue
            if constants.END_OF_DATA == raw:
                break
            if flag:
                data.append(raw.split(constants.DELIMITER)[:-1])

        df = pd.DataFrame(columns=fields, data=data)
        return df

    def parse_reference_field(self):
        """
        read reference fields and put it into dataframe
        :return: reference fields in dataframe
        """
        field_df = pd.read_csv(self.reference_field)
        return field_df['field']

    def parse_reference_data(self):
        """
        read reference data and put it into dataframe
        :return: reference data in dataframe
        """
        refer_data = pd.read_csv(self.reference_data)
        return refer_data

    def parse_vendor_field(self):
        """
        parse the fields in the input file
        :return: fields in the input file
        """
        fields = []
        flag = False
        for line in skip_comments(self.vendor_file):
            raw = line.decode().rstrip()
            if constants.START_OF_FIELDS == raw:
                flag = True
                continue
            if constants.END_OF_FIELDS == raw:
                break
            if flag and raw != "":
                fields.append(raw)
        return fields
