import pandas as pd
import argparse

# aircraft data
# name, passenger number, overall length[m], width[m], height[m], fuselage width[m], fuselage height[m],
# max takeoff weight[kg], max landing weight[kg], max zero fuel weight[kg], cargo volume[m^3], cruise mach,
# cruise altitude[m], cruise range[km], lift by drag(L/D), wing area[m^2], aspect ratio(AR), retreat angle,
# ratio of thickness and chord, vertical wing width[m], horizontal wing width[m]

# engine data
# name, takeoff thrust[N], cruise thrust[N], BPR, OPR, FPR, TIT, engine weight[kg], fuel type, fan stage number,
# lpc stage number, hpc stage number, hpt stage number, lpt stage number, fan stage load factor,
# lpc stage load factor, hpc stage load factor, hpt stage load factor, lpt stage load factor, fan diameter[m],
# engine length[m], ratio of thrust and weight

def replace_database(name, data, path):
    """
    change the contents of database

    :param name: string, ex) "A320", "CFM56"
    :param data: list, the set of necessary variables for constructing data base
    :param path: string, path of data base
    :return: None
    """

    df = pd.read_csv(path, index_col=0)
    df.loc[name] = data
    df.to_csv(path)


def construct_aircraft_data(args):
    """
    create the set of aircraft data
    :param args: parser argument class
    :return: aircraft_name(string), aircraft_data(list)
    """
    aircraft_name = args.aircraft_name
    aircraft_data = [args.passenger_number,
                     args.overall_length,
                     args.width,
                     args.height,
                     args.fuselage_width,
                     args.fuselage_height,
                     args.max_takeoff_weight,
                     args.max_landing_weight,
                     args.max_zero_fuel_weight,
                     args.cargo_volume,
                     args.cruise_mach,
                     args.cruise_altitude,
                     args.cruise_range,
                     args.lift_by_drag,
                     args.wing_area,
                     args.aspect_ratio,
                     args.rectangle_angle,
                     args.ratio_of_thickness_and_chord,
                     args.vertical_wing_width,
                     args.horizontal_wing_width]

    return aircraft_name, aircraft_data


def construct_engine_data(args):
    """
    create the set of engine data

    :param args: parser argument class
    :return: engine_name(string), engine_data(list)
    """

    engine_name = args.engine_name

    engine_data = [args.takeoff_thrust,
                   args.cruise_thrust,
                   args.BPR,
                   args.OPR,
                   args.FPR,
                   args.TIT,
                   args.engine_weight,
                   args.fuel_type,
                   args.fan_stage_number,
                   args.lpc_stage_number,
                   args.hpc_stage_number,
                   args.hpt_stage_number,
                   args.lpt_stage_number,
                   args.lpc_stage_load_factor,
                   args.hpc_stage_load_factor,
                   args.hpt_stage_load_factor,
                   args.lpt_stage_load_factor,
                   args.fan_diameter,
                   args.engine_length,
                   args.ratio_of_thrust_and_weight]

    return engine_name, engine_data



class DataDriven(object):
    """
    Params:
        aircraft name:
             type(string)
        passenger number:
             the number of passenger on boarding
             type(int)
        overall length:
             the overall length of aircraft's fuselage[m]
             type(float)
        width: wing width[m], formally represent "b"
               type(float)
    height: aircraft height[m]
           type(float)
    fuselage width: the width of fuselage[m]
                    type(float)
    fuselage height: the height of fuselage[m]
                     type(float)
    max takeoff weight: max takeoff weight[kg]
                        type(float)
    max landing weight: max landing weight[kg]
                        type(float)
    max zero fuel weight: the weight without fuel weight[kg]
                          type(float)
    cargo volume: the volume of cargo shelter[m^3]
                  type(float)
    cruise mach: mach number at cruise phase (no dimension)
                 type(float)
    cruise altitude: altitude at cruise phase[m]
                     type(float)
    cruise range: max cruise range[km]
                  type(float)
    lift by drag: lift by drag at cruise point, in particular, the ratio of thrust and total weight is equal to L/D
                  type(float)
    wing area: Area of wing, which formally represents "S", [m^2]
    aspect ratio: AR = b ** 2 / S
    retreat angle: retreat angle, which formally upper delta
    ratio of thickness and chord: t / c(t = thickness, c= chord)
    vertical wing width: vertical wing width[m], formally represents bv
    horizontal wing width: horizontal wing width[m], formally represents bh

    """

    def __init__(self, args):

        # the content of aircraft data base
        self.aircraft_columns = ['aircraft_name',
                                 'passenger_number',
                                 'overall_length',
                                 'width',
                                 'height',
                                 'fuselage_width',
                                 'fuselage_height',
                                 'max_takeoff_weight',
                                 'max_landing_weight',
                                 'max_zero_fuel_weight',
                                 'cargo_volume',
                                 'cruise_mach',
                                 'cruise_altitude',
                                 'cruise_range',
                                 'lift_by_drag',
                                 'wing_area',
                                 'aspect_ratio',
                                 'rectangle_angle',
                                 'ratio_of_thickness_and_chord',
                                 'vertical_wing_width',
                                 'horizontal_wing_width']
        # the content of engine data base
        self.engine_columns = ['engine_name',
                               'takeoff_thrust',
                               'cruise_thrust',
                               'BPR',
                               'OPR',
                               'FPR',
                               'TIT',
                               'engine_weight',
                               'fuel_type',
                               'fan_stage_number',
                               'lpc_stage_number',
                               'hpc_stage_number',
                               'hpt_stage_number',
                               'lpt_stage_number',
                               'lpc_stage_load_factor',
                               'hpc_stage_load_factor',
                               'hpt_stage_load_factor',
                               'lpt_stage_load_factor',
                               'fan_diameter',
                               'engine_length',
                               'ratio_of_thrust_and_weight']

        # aircraft and engine data path
        self.aircraft_data_path = './DataBase/aircraft.csv'
        self.engine_data_path = './DataBase/engine.csv'

        # set the dataframe
        # aircraft
        aircraft_name, aircraft_data = construct_aircraft_data(args)
        replace_database(aircraft_name, aircraft_data, self.aircraft_data_path)

        # engine
        engine_name, engine_data = construct_engine_data(args)
        replace_database(engine_name, engine_data, self.engine_data_path)


if __name__ == '__main__':
    # build parser class
    parser = argparse.ArgumentParser()

    # add arguments
    # aircraft
    parser.add_argument('--aircraft_name', default='A322', type=str)
    parser.add_argument('--passenger_number', default=150, type=int)
    parser.add_argument('--overall_length', default=37.57, type=float)
    parser.add_argument('--width', default=34.10, type=float)
    parser.add_argument('--height', default=11.76, type=float)
    parser.add_argument('--fuselage_width', default=3.95, type=float)
    parser.add_argument('--fuselage_height', default=4.14, type=float)
    parser.add_argument('--max_takeoff_weight', default=78000, type=float)
    parser.add_argument('--max_landing_weight', default=66000, type=float)
    parser.add_argument('--max_zero_fuel_weight', default=60000, type=float)
    parser.add_argument('--cargo_volume', default=37.42, type=float)
    parser.add_argument('--cruise_mach', default=0.82, type=float)
    parser.add_argument('--cruise_altitude', default=10668, type=float)
    parser.add_argument('--cruise_range', default=6400, type=float)
    parser.add_argument('--lift_by_drag', default=17, type=float)
    parser.add_argument('--wing_area', default=122.6, type=float)
    parser.add_argument('--aspect_ratio', default=9.5, type=float)
    parser.add_argument('--rectangle_angle', default=25, type=float)
    parser.add_argument('--ratio_of_thickness_and_chord', default=0.15, type=float)
    parser.add_argument('--vertical_wing_width', default=5.87, type=float)
    parser.add_argument('--horizontal_wing_width', default=12.45, type=float)

    # engine
    parser.add_argument('--engine_name', default='CFM56-B', type=str)
    parser.add_argument('--takeoff_thrust', default=120000, type=float)
    parser.add_argument('--cruise_thrust', default=21000, type=float)
    parser.add_argument('--BPR', default=5.7, type=float)
    parser.add_argument('--OPR', default=32.6, type=float)
    parser.add_argument('--FPR', default=1.6, type=float)
    parser.add_argument('--TIT', default=1400, type=float)
    parser.add_argument('--engine_weight', default=2380, type=float)
    parser.add_argument('--fuel_type', default='jet', type=str, help='jet, hydrogen, bio, solar')
    parser.add_argument('--fan_stage_number', default=1, type=float)
    parser.add_argument('--lpc_stage_number', default=3, type=float)
    parser.add_argument('--hpc_stage_number', default=9, type=float)
    parser.add_argument('--hpt_stage_number', default=1, type=float)
    parser.add_argument('--lpt_stage_number', default=4, type=float)
    parser.add_argument('--lpc_stage_load_factor', default=0.17, type=float)
    parser.add_argument('--hpc_stage_load_factor', default=0.3, type=float)
    parser.add_argument('--hpt_stage_load_factor', default=1.2, type=float)
    parser.add_argument('--lpt_stage_load_factor', default=1.2, type=float)
    parser.add_argument('--fan_diameter', default=1.74, type=float)
    parser.add_argument('--engine_length', default=2.51, type=float)
    parser.add_argument('--ratio_of_thrust_and_weight', default=3.7, type=float)

    # build argument class
    args = parser.parse_args()

    # build data driven class
    ddc = DataDriven(args)

