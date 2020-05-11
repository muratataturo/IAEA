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

        # Initialize parameters
        # deal with following value by ft or kg

        # fuselage
        # fuselage is divided into three section(section1: cockpit, section2: cabin, section3: after cabin)
        self.cockpit_length = None  # l1
        self.cabin_length = None  # l2
        self.after_cabin_length = None  # l3
        self.fuselage_length = None  # l1 + l2 + l3

        self.cockpit_width = None  # w1
        self.cabin_width = None  # w2(df)
        self.after_cabin_length = None  # w3

        # Note: cockpit and after cabin shapes are circle
        self.cockpit_upper_height = None  # the height of upper part of cockpit
        self.cockpit_lower_height = None  # the height of lower part of cockpit
        self.cabin_upper_height = None  # the height of fuselage which contains passenger
        self.cabin_lower_height = None  # the height of fuselage which is determined by cargo fuselage
        self.after_cabin_upper_height = None  # the height of upper part of after cabin
        self.after_cabin_lower_height = None  # hte height of lower part of after cabin
        self.KWs = None  # costant => 0.75 * ((1.0 + 2.0 * taper ratio) / (1.0 + taper ratio)) * (main wing span * np.tan(25 * wingsweep_theta / fuselage length))

        # main wing
        self.main_wing_span = None  # wing span(b)
        self.main_wing_aspect_ratio = None  # AR
        self.main_wing_taper_ratio = None  # t
        self.main_wing_tc = None  # the ratio of thickness and chord
        self.retreat_angle = None  # theta
        self.main_wing_croot = None  # the root chord of main wing
        self.main_wing_ctip = None  # the tip chord of main wing
        self.main_wing_area = None  # S
        self.Nz = None  # ultimate load coefficient

        # vertical wing
        self.vertical_wing_span = None  # wing span(bv)
        self.vertical_wing_aspect_ratio = None  # ARv
        self.vertical_wing_taper_ratio = None  # tv
        self.vertical_wing_tc = None  # the ratio of thickness and chord at vertical wing
        self.vertical_retreat_angle = None  # thetav
        self.vertical_wing_croot = None  # the root chord of vertical wing
        self.vertical_wing_ctip = None  # the tip chord of vertical wing
        self.vertical_wing_area = None  # Sv

        # vertical wing
        self.horizontal_wing_span = None  # wing span(bh)
        self.horizontal_wing_aspect_ratio = None  # ARh
        self.horizontal_wing_taper_ratio = None  # th
        self.horizontal_wing_tc = None  # the ratio of thickness and chord at horizontal wing
        self.horizontal_retreat_angle = None  # thetah
        self.horizontal_wing_croot = None  # the root chord of horizontal wing
        self.horizontal_wing_ctip = None  # the tip chord of horizontal wing
        self.horizontal_wing_area = None  # Sh

        # main landing gear
        self.main_landing_gear_position = None  # the setting position of main landing gear(Lm)
        self.number_of_main_wheel = None  # the number of main wheel
        self.number_of_main_gear_struts = None  # the number of main gear struts
        self.Vstall = 130  # stall velocity

        # Nose landing gear
        self.nose_landing_gear_position = None  # the setting position of nose landing gear(Ln)
        self.number_of_nose_wheel = None  # the number of nose wheel

        # Nacelle
        self.engine_number = None  # the number of jet engine

        # Engine Control
        self.engine_control_position = None  # the mounting position of engine control

        # Flight Control
        self.number_of_flight_control = None  # the number of flight control
        self.exposed_wing_span = None  # outer wing span (BW)

        # Instrument
        self.number_of_instrument = None  # the number of instrument, jet engine(2.0), UAV(0.5)


    def setting_for_computation(self):
        """

        calculate aircraft's configurations from given design variables
        :return: None
        """
        pass


    def setting_for_view_by_database(self):

        pass


    def setting_for_view_by_optimization(self):
        """

        :return: None
        """

        pass



if __name__ == '__main__':

    aircraft_name = "A320"
    ap = AircraftParams(aircraft_name)



