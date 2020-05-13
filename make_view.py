import pandas as pd
import argparse

# create aircraft file which has configurations for view
def create_aircraft_view_file(args):
    aircraft_view_path = './View/AircraftView/'
    # create file
    if args.aircraft_name:
        f = open(aircraft_view_path + args.aircraft_name + '.csv', 'w')
        f.close()



# create engine file which has configurations for view
def create_engine_view_file(args):
    engine_view_path = './View/EngineView/'
    # create file
    if args.engine_name:
        f = open(engine_view_path + args.engine_name + '.csv', 'w')
        f.close()
    pass




parser = argparse.ArgumentParser()
parser.add_argument('--aircraft_name', default='A320', type=str)
parser.add_argument('--engine_name', default='CFM56', type=str)

args = parser.parse_args()

# view columns
aircraft_view_columns = ['cockpit_length', 'cabin_length', 'after_cabin_length', 'fuselage_length',
                        'cockpit_width', 'cabin_width',  'after_cabin_width', 'cockpit_upper_height',
                        'cockpit_lower_height', 'cabin_upper_height', 'cabin_lower_height', 'after_cabin_upper_height',
                        'after_cabin_lower_height', 'KWs',
                        'main_wing_span', 'main_wing_aspect_ratio', 'main_wing_taper_ratio', 'main_wing_tc',
                        'retreat_angle', 'main_wing_croot', 'main_wing_ctip', 'main_wing_area',
                        'vertical_wing_span', 'vertical_wing_aspect_ratio', 'vertical_wing_taper_ratio',
                        'vertical_wing_tc', 'vertical_retreat_angle', 'vertical_wing_croot', 'vertical_wing_ctip',
                        'vertical_wing_area',
                        'horizontal_wing_span', 'horizontal_wing_aspect_ratio', 'horizontal_wing_taper_ratio',
                        'horizontal_wing_tc', 'horizontal_retreat_angle', 'horizontal_wing_croot',
                        'horizontal_wing_ctip', 'horizontal_wing_area',
                        'main_landing_gear_position', 'number_of_main_wheel', 'number_of_main_gear_struts', 'Vstall',
                        'nose_landing_gear_position', 'number_of_nose_wheel',
                        'engine_number',
                        'engine_control_position',
                        'number_of_flight_control',
                        'exposed_wing_span',
                        'number_of_instrument']



