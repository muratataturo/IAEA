

class DesignVariablesController(object):

    def __init__(self, aircraft_params_class, engine_params_class):

        # Parameter class
        self.aircraft_params_class = aircraft_params_class
        self.engine_params_class = engine_params_class

        # set aircraft parameter from design variables



def main():

    design_variables = []

    # aircraft design variables
    aircraft_fuselage_dvs = [cabin_length, s1_h, s2_h, s3_h, s1_v, s2_v, s3_v]

    fl_bs_index, fl_bf_index = 0, len(aircraft_fuselage_dvs)

    aircraft_wing_dvs = [bm, ARm, tm, tcm, thetam, bh, ARh, th, tch, thetah, bv, ARv, tv, tcv, thetav]

    w_bs_index, w_bf_index = fl_bf_index, len(aircraft_wing_dvs) + fl_bf_index

    aircraft_performance_dvs = [aoa]

    pf_bs_index, pf_bf_index = w_bf_index, w_bf_index + len(aircraft_performance_dvs)


    # engine design variables

    engine_dvs = [OPR, TIT, BPR, FPR, Nen, tech_lev, cool_air_lpt, cool_air_hpt, engine_material_quality,
                  fan_sn, lpc_sn, hpc_sn, hpt_sn, lpt_sn, fan_lf, lpc_lf, hpc_lf, hpt_lf, lpt_lf,
                  BPRe, FPRe, Nfan, eng_electriceff, eng_electric_dense]

    ed_bs_index, ed_bf_index = pf_bf_index, pf_bf_index + len(engine_dvs)

    # joint design variables
    # aircraft
    aircraft_mounting_dvs = [cmx, cmz, chx, chz, cbx, cbz]

    am_bs_index, am_bf_index = ed_bf_index, ed_bf_index + len(aircraft_mounting_dvs)

    # engine
    engine_mounting_dvs = [ecmx, ecmy, theta_ec, sign_ec, edmx, edmy, theta_ed, sign_ed]

    em_bs_index, em_bf_index = am_bf_index, am_bf_index + len(engine_mounting_dvs)

    # BLI
    bli_dvs = [dist_ang]

    bl_bs_index, bl_bf_index = em_bf_index, em_bf_index + len(bli_dvs)

    # electric
    electric_dvs = [mat_lev, bat_ele_dense]

    ele_bs_index, ele_bf_index = bl_bf_index, bl_bf_index + len(electric_dvs)

    # mission
    mission_dvs = [altitude, mach_number, thrust_doff, ld, cruise_range, mtow, passenger_num, fuel_coef, cargo_weight, cargo_volume]

    mis_bs_index, mis_bf_index = ele_bf_index, ele_bf_index + len(mission_dvs)








if __name__ == '__main__':
    main()

