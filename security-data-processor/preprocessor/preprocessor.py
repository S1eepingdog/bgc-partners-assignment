from datetime import datetime

from .parser import Parser
from .utils import *


class ReferencePreprocessor(object):
    def __init__(self, input_file="corp_pfd.dif", reference_field="reference_fields.csv",
                 reference_data="reference_securities.csv", new_security_filename="new_securities.csv",
                 security_data_filename="security_data.csv"):
        self.parser = Parser(input_file, reference_field, reference_data)
        self.input_file = input_file
        self.new_security_filename = new_security_filename
        self.security_data_filename = security_data_filename

    def process(self):
        """
        1. load and parse the file
        2. limit input data with reference columns
        3. find new securities and output to csv
        4. output the input data to column-based csv
        """
        # load data and fields from file to dataframe
        vendor_data = self.parser.parse_vendor_data()
        reference_data = self.parser.parse_reference_data()
        reference_field = self.parser.parse_reference_field()

        # find data not in reference file
        limit_data = vendor_data[vendor_data.columns.intersection(reference_field)]
        new_data = limit_data[~limit_data.ID_BB_GLOBAL.isin(reference_data['id_bb_global'])]
        new_data.columns = new_data.columns.str.lower()
        output(new_data[reference_data.columns], self.new_security_filename)

        # convert input data to column-based dataframe
        # and add input file name and timestamp
        security_data = limit_data.melt(id_vars='ID_BB_GLOBAL', var_name="FIELD", value_name="VALUE")
        security_data['SOURCE'] = self.input_file
        dt = datetime.now()
        security_data['TSTAMP'] = dt.strftime("%Y-%m-%d %H:%M:%S")
        output(security_data, self.security_data_filename)
