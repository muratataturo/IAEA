import pandas as pd


class AircraftParams(object):
    """
    --Attributes--
        aircraft name:
           type(string)

        aircraft database path:
           type(string), path of aircraft database path
    """

    def __init__(self, aircraft_name):

        self.aircraft_name = aircraft_name

        # path of aircraft database
        self.aircraft_database_path = "./DataBase/aircraft.csv"

        df = pd.read_csv(self.aircraft_database_path, index_col=0)

        print(df.columns)  # extract column
        print(df.loc[self.aircraft_name].values)  # extract numpy array from database


    def setting(self):
        """

        :return: None
        """
        pass



if __name__ == '__main__':

    aircraft_name = "A320"
    ap = AircraftParams(aircraft_name)


