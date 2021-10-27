import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer


class preprocessing():

    def __init__(self , file_object , logger_object):
        self.file_object = file_object
        self.logger_object = logger_object

    def remove_columns(self,data,columns):
        """
                Method Name : remove columns
                params : file_object , logger_object
                removes columns from the data
        
        """

        self.logger_object.log(self.file_object, 'Entered the remove colums method of preprocessing class')
        self.data = data
        self.columns = columns

        try:
            self.useful_data = self.data.drop(labels = self.columns, axix = 1)
            self.logger_object.log(self.file_object,)
    