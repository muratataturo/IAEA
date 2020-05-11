
class DesignVariable(object):
    """
    Note:
        if you want to view aircraft or engine, you should set real value and boundary condition
        if you want to optimize aircraft or engine, you should set normalized value and boundary condition
    """

    def __init__(self, name):
        # design variable name
        self.name = name
        # real value
        self.val = None
        # normalized value(0~1)
        self.norm_val = None
        # boundary condition
        self.bound = [None, None]  # [minimum, maximum]

    def set_bound(self, bounds):
        """
        set boundary condition

        :param bounds: [minimum value, maximum value]
        :return: None
        """
        self.bound[0], self.bound[1] = bounds[0], bounds[1]

    def set_val(self, val):
        """
        set design variable's real value

        :param val: the value of design variable
        :return: None
        """

        self.val = val

    def set_norm_val(self, norm_val):
        """
        set design variable normalized value

        :param norm_val: the normalized value of design variable
        :return: None
        """

        self.norm_val = norm_val

    def normalize(self):
        """
        normalize real value

        :return: None
        """
        self.norm_val = (self.val - self.bound[0]) / (self.bound[1] - self.bound[0])

    def denormalize(self):
        """
        convert normalized value into real value

        :return:
        """

        self.val = self.bound[0] + self.norm_val * (self.bound[1] - self.bound[0])


class DesignVariablesController(object):

    def __init__(self, aircraft_params_class, engine_params_class):

        # Parameter class
        self.aircraft_params_class = aircraft_params_class
        self.engine_params_class = engine_params_class

        # set aircraft parameter from design variables



def main():

    design_variables = []

    # aircraft design variables
    # fuselage part
    aircraft_fuselage_dv_names = ['fuselage_length', 's1_h', 's2_h', 's3_h', 's1_v', 's2_v', 's3_v']
    aircraft_fuselage_boundaries = [[30, 40], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]
    fuselage_length = 37.57  # [m]
    s1_h = 0.05
    s2_h = 0.105
    s3_h = 0.05
    s1_v = 0.2
    s2_v = 0.6
    s3_v = 0.2
    aircraft_fuselage_dvs = [fuselage_length, s1_h, s2_h, s3_h, s1_v, s2_v, s3_v]

    # Initialize design variables set
    fl_dv_sets = [DesignVariable(name) for name in aircraft_fuselage_dv_names]

    # set design variable class
    for idx, fd in enumerate(fl_dv_sets):
        # set design variables
        fd.set_val(aircraft_fuselage_dvs[idx])
        # set boundaries
        fd.set_bound(aircraft_fuselage_boundaries[idx])

    print(fl_dv_sets[0].val)

    fl_bs_index, fl_bf_index = 0, len(aircraft_fuselage_dvs)

    # wing part
    aircraft_wing_dv_names = ['main wing span', 'main wing AR', 'main wing taper ratio', 'main wing tc ratio',
                              'main wing retreat angle', 'horizontal wing span', 'horizontal wing aspect ratio',
                              'horizontal wing taper ratio', 'horizontal wing tc ratio',
                              'horizontal wing retreat angle', 'vertical wing span', 'vertical wing AR',
                              'vertical wing taper ratio', 'vertical wing tc ratio', 'vertical wing retreat angle']

    aircraft_wing_boundaries = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    bm = 0
    ARm = 0
    tm = 0
    tcm = 0
    thetam = 0
    bh = 0
    ARh = 0
    th = 0
    tch = 0
    thetah = 0
    bv = 0
    ARv = 0
    tv = 0
    tcv = 0
    thetav = 0

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

