import pandas as pd


class EngineParams(object):
    """
    --Attributes--

        engine name:
           type(string)

        engine database path:
           type(string), path of aircraft database path

    """

    def __init__(self, engine_name):

        self.engine_name = engine_name

        self.engine_database_path = "./DataBase/engine.csv"

        df = pd.read_csv(self.engine_database_path, index_col=0)

        print(df.columns)  # extract columns
        print(df.loc[self.engine_name].values)  # extract numpy array from database

    def setting(self):
        """

        :return: None
        """
        pass




if __name__ == '__main__':

    engine_name = "CFM56"
    ep = EngineParams(engine_name)