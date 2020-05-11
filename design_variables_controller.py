# Base design variable class
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
        # fixed flag
        self.fix = False

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

    def fixed(self, fix_flag):
        """

        :param fix_flag: boolean
        :return: None
        """

        self.fix = fix_flag

        if self.fix:
            self.bound = [self.val, self.val]


# Aircraft fuselage design variables class
class AircraftFuselageDesignVariable(object):
    """
    Note:
        Design Variable Controller Class for Aircraft Fuselage

    --Attributes--
        aircraft_fuselage_dv_names: list
            the list of fuselage design variables

        aircraft_fuselage_dv_idx_dict: dict
            dictionary in order to change name into index number

        fuselage_dv_num: int
            the number of fuselage design variables

        aircraft_fuselage_boundaries: list[list]
            the list which keeps the bounds list

        aircraft_fuselage_fix_flags: list[bool]
            the list which keeps boolean flag which indicates whether or not the value is fixed

        fl_dv_sets: list[DesignVariableClass]
            the list of design variable class

    --Method--
        set_bounds()

        set_fix()

        create_dv_sets()

    """

    def __init__(self):
        self.aircraft_fuselage_dv_names = ['fuselage_length', 's1_h', 's2_h', 's3_h', 's1_v', 's2_v', 's3_v']
        self.aircraft_fuselage_dv_idx_dict = {}
        for idx, name in enumerate(self.aircraft_fuselage_dv_names):
            self.aircraft_fuselage_dv_idx_dict[name] = idx
        self.fuselage_dv_num = len(self.aircraft_fuselage_dv_names)
        self.aircraft_fuselage_boundaries = [[30, 40], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]
        self.aircraft_fuselage_fix_flags = [False for _ in range(self.fuselage_dv_num)]

        # Initialize design variables set
        self.fl_dv_sets = [DesignVariable(name) for name in self.aircraft_fuselage_dv_names]

    def set_bounds(self, name, bounds):
        """

        :param name: str
               design variable name
        :param bounds: list
               list of boundary condition(min, max)
        :return: None
        """
        idx = self.aircraft_fuselage_dv_idx_dict[name]
        self.aircraft_fuselage_boundaries[idx] = bounds

    def set_fix(self, name, flag=True):
        """

        :param name: str
               design variable name
        :param flag: bool
               flag which means fix
        :return: None
        """
        idx = self.aircraft_fuselage_dv_idx_dict[name]
        self.aircraft_fuselage_fix_flags[idx] = flag

    def create_dv_sets(self, aircraft_fuselage_dvs):
        """

        :param aircraft_fuselage_dvs: list
               design variables vector
        :return: None
        """

        # set design variable class
        for idx, fd in enumerate(self.fl_dv_sets):
            # set design variables
            fd.set_val(aircraft_fuselage_dvs[idx])
            # set boundaries
            fd.set_bound(self.aircraft_fuselage_boundaries[idx])
            # set fixed flag
            fd.fixed(self.aircraft_fuselage_fix_flags[idx])


# Aircraft wing design variable class
class AircraftWingDesignVariable(object):

    def __init__(self):
        self.aircraft_wing_dv_names = ['main wing span', 'main wing AR', 'main wing taper ratio', 'main wing tc ratio',
                                  'main wing retreat angle', 'horizontal wing span', 'horizontal wing aspect ratio',
                                  'horizontal wing taper ratio', 'horizontal wing tc ratio',
                                  'horizontal wing retreat angle', 'vertical wing span', 'vertical wing AR',
                                  'vertical wing taper ratio', 'vertical wing tc ratio', 'vertical wing retreat angle']

        self.aircraft_wing_boundaries = [[30, 40],
                                    [8, 10],
                                    [0.2, 0.3],
                                    [0.1, 0.2],
                                    [20, 30],
                                    [10, 15],
                                    [1.5, 3.0],
                                    [0.2, 0.3],
                                    [0.1, 0.2],
                                    [25, 35],
                                    [5, 10],
                                    [1.0, 2.0],
                                    [0.2, 0.3],
                                    [0.1, 0.2],
                                    [40, 50]]

        self.aircraft_wing_dv_num = len(self.aircraft_wing_dv_names)

        self.aircraft_wing_fix_flags = [False for _ in range(self.aircraft_wing_dv_num)]

    def set_bounds(self, name, bounds):
        pass

    def set_fix(self, name, flag=True):
        pass

    def create_dv_sets(self, aircraft_wing_dvs):
        pass

# Aircraft performance design variable class
class AircraftPerformanceDesignVariable(object):

    def __init__(self):
        pass

# Engine design variable class
class EngineDesignVariable(object):

    def __init__(self):
        pass

# Joint Aircraft design variable class
class JointAircraftDesignVariable(object):

    def __init__(self):
        pass

# Joint Engine design variable class
class JointEngineDesignVariable(object):

    def __init__(self):
        pass

# BLI design variable class
class BLIDesignVariable(object):

    def __init__(self):
        pass

# Mission design variable class
class MissionDesignVariable(object):

    def __init__(self):
        pass



# Integration Design Variables Controller
class DesignVariablesController(object):

    def __init__(self, aircraft_params_class, engine_params_class):

        # Parameter class
        self.aircraft_params_class = aircraft_params_class
        self.engine_params_class = engine_params_class

        # set aircraft parameter from design variables


# test code
def main():
    # build aircraft fuselage design variable class
    fuselage_length = 37.57  # [m]
    s1_h = 0.05  # section 1 horizontal coefficient
    s2_h = 0.105  # section 2 horizontal coefficient
    s3_h = 0.05  # section 3 horizontal coefficient
    s1_v = 0.2  # section 1 vertical coefficient
    s2_v = 0.6  # section 2 vertical coefficient
    s3_v = 0.2  # section 3 vertical coefficient
    aircraft_fuselage_dvs = [fuselage_length, s1_h, s2_h, s3_h, s1_v, s2_v, s3_v]

    # Initialization
    afdv = AircraftFuselageDesignVariable()
    # create the sets of design variables
    afdv.create_dv_sets(aircraft_fuselage_dvs)

    # confirmation
    print('')
    print('aircraft fuselage class')
    for u in afdv.fl_dv_sets:
        print(u.val)
        print(u.bound)
        print(u.fix)
    print('')

    # build aircraft wing design variable class

    # build aircraft performance design variable class

    # build joint aircraft design variable class

    # build joint engine design variable class

    # build BLI design variable class

    # build mission design variable class

    pass


def main_():

    # unit change
    m_to_ft = 3.28084
    kg_to_lb = 2.204621

    design_variables = []

    # aircraft design variables
    # fuselage part, section1: cockpit, section2: cabin, section3: after cabin
    aircraft_fuselage_dv_names = ['fuselage_length', 's1_h', 's2_h', 's3_h', 's1_v', 's2_v', 's3_v']
    aircraft_fuselage_boundaries = [[30, 40], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]
    aircraft_fuselage_fixed_flags = [False, False, False, False, False, False, False]
    fuselage_length = 37.57  # [m]
    s1_h = 0.05  # section 1 horizontal coefficient
    s2_h = 0.105  # section 2 horizontal coefficient
    s3_h = 0.05  # section 3 horizontal coefficient
    s1_v = 0.2  # section 1 vertical coefficient
    s2_v = 0.6  # section 2 vertical coefficient
    s3_v = 0.2  # section 3 vertical coefficient
    aircraft_fuselage_dvs = [fuselage_length, s1_h, s2_h, s3_h, s1_v, s2_v, s3_v]

    # Initialize design variables set
    fl_dv_sets = [DesignVariable(name) for name in aircraft_fuselage_dv_names]

    # set design variable class
    for idx, fd in enumerate(fl_dv_sets):
        # set design variables
        fd.set_val(aircraft_fuselage_dvs[idx])
        # set boundaries
        fd.set_bound(aircraft_fuselage_boundaries[idx])
        # set fixed flag
        fd.fixed(aircraft_fuselage_fixed_flags[idx])

    print(fl_dv_sets[0].val)
    print(fl_dv_sets[0].bound)
    print(fl_dv_sets[0].fix)

    fl_bs_index, fl_bf_index = 0, len(aircraft_fuselage_dvs)


    # wing part
    aircraft_wing_dv_names = ['main wing span', 'main wing AR', 'main wing taper ratio', 'main wing tc ratio',
                              'main wing retreat angle', 'horizontal wing span', 'horizontal wing aspect ratio',
                              'horizontal wing taper ratio', 'horizontal wing tc ratio',
                              'horizontal wing retreat angle', 'vertical wing span', 'vertical wing AR',
                              'vertical wing taper ratio', 'vertical wing tc ratio', 'vertical wing retreat angle']


    aircraft_wing_boundaries = [[30, 40],
                                [8, 10],
                                [0.2, 0.3],
                                [0.1, 0.2],
                                [20, 30],
                                [10, 15],
                                [1.5, 3.0],
                                [0.2, 0.3],
                                [0.1, 0.2],
                                [25, 35],
                                [5, 10],
                                [1.0, 2.0],
                                [0.2, 0.3],
                                [0.1, 0.2],
                                [40, 50]]

    aircraft_wing_dv_num = len(aircraft_wing_dv_names)

    aircraft_wing_fixed_flags = [False for _ in range(aircraft_wing_dv_num)]

    bm = 34.1  # main wing span [m]
    ARm = 9.5  # main wing aspect ratio
    tm = 0.24  # taper ratio
    tcm = 0.11  # the ratio of thickness and chord at main wing
    thetam = 25.0  # retreat angle of main wing[rad]
    # horizontal
    bh = 12.45
    ARh = 2.0
    th = 0.24
    tch = 0.11
    thetah = 31.0
    # vertical
    bv = 5.87
    ARv = 1.2
    tv = 0.24
    tcv = 0.15
    thetav = 49.0

    aircraft_wing_dvs = [bm, ARm, tm, tcm, thetam, bh, ARh, th, tch, thetah, bv, ARv, tv, tcv, thetav]

    # Initialize aircraft wing dv sets
    aw_dv_sets = [DesignVariable(name) for name in aircraft_wing_dv_names]

    # set aircraft wing dv sets
    for idx, ad in enumerate(aw_dv_sets):

        ad.set_val(aircraft_wing_dvs[idx])
        ad.set_bound(aircraft_wing_boundaries[idx])
        ad.fixed(aircraft_wing_fixed_flags[idx])

    w_bs_index, w_bf_index = fl_bf_index, len(aircraft_wing_dvs) + fl_bf_index


    # aircraft performance part
    aircraft_performance_dv_names = ['attack of angle']
    aircraft_performance_boundaries = [[0, 6]]
    aoa = 4  # attack of angle
    aircraft_performance_dvs = [aoa]

    # Initialize the aircraft performance dv sets
    ap_dv_sets = [DesignVariable(name) for name in aircraft_performance_dv_names]

    for idx, ad in enumerate(ap_dv_sets):

        ad.set_val(aircraft_performance_dvs[idx])
        ad.set_bound(aircraft_performance_boundaries[idx])

    pf_bs_index, pf_bf_index = w_bf_index, w_bf_index + len(aircraft_performance_dvs)


    # engine design variables

    engine_dv_names = ['OPR', 'TIT', 'BPR', 'FPR', 'Nen', 'technical level', 'cool air lpt rate', 'cool air hpt rate',
                       'engine material quality', 'fan stage number', 'lpc stage number', 'hpc stage number',
                       'hpt stage number', 'lpt stage number', 'fan load factor', 'lpc load factor', 'hpc load factor',
                       'hpt load factor', 'lpt load factor', 'BPRe', 'FPRe', 'Nfan', 'engine electric efficiency',
                       'engine electric density']

    engine_boundaries = [[20, 40],  # OPR
                         [1200, 1500],  # TIT
                         [2, 8],  # BPR
                         [1.2, 1.7],  # FPR
                         [1, 4],  # Nen
                         [3, 4],  # tech lev
                         [0.0, 0.1],  # cool air lpt
                         [0.0, 0.2],  # cool air hpt
                         [0.5, 1.0],  # engine material quality
                         [1, 2],  # fan stage number
                         [2, 4],  # lpc stage number
                         [8, 10],  # hpc stage number
                         [1, 3],  # hpt stage number
                         [1, 5],  # lpt stage number
                         [0.1, 0.4],  # fan load factor
                         [0.1, 0.4],  # lpc load factor
                         [0.3, 0.5],  # hpc load factor
                         [1.3, 1.6],  # hpt load factor
                         [1.3, 1.6],  # lpt load factor
                         [0, 10],  # BPRe
                         [0, 1.5],  # FPRe
                         [1, 10],  # Nfan
                         [0.9, 0.99],  # eng_electriceff
                         [0.052, 0.52]  # eng_electric_dense
                         ]

    engine_dv_num = len(engine_dv_names)

    engine_fix_flags = [False for _ in range(engine_dv_num)]

    OPR = 30
    TIT = 1400
    BPR = 6.0
    FPR = 1.4
    Nen = 2
    tech_lev = 3
    cool_air_lpt = 0
    cool_air_hpt = 0.15
    engine_material_quality = 1.0
    fan_sn = 1
    lpc_sn = 2
    hpc_sn = 10
    hpt_sn = 1
    lpt_sn = 3
    fan_lf = 0.2
    lpc_lf = 0.2
    hpc_lf = 0.4
    hpt_lf = 1.5
    lpt_lf = 1.5
    BPRe = 0
    FPRe = 0
    Nfan = 0
    eng_electriceff = 0.9
    eng_electric_dense = 0.52

    engine_dvs = [OPR, TIT, BPR, FPR, Nen, tech_lev, cool_air_lpt, cool_air_hpt, engine_material_quality,
                  fan_sn, lpc_sn, hpc_sn, hpt_sn, lpt_sn, fan_lf, lpc_lf, hpc_lf, hpt_lf, lpt_lf,
                  BPRe, FPRe, Nfan, eng_electriceff, eng_electric_dense]

    e_dv_sets = [DesignVariable(name) for name in engine_dv_names]

    for idx, ed in enumerate(e_dv_sets):

        ed.set_val(engine_dvs[idx])
        ed.set_bound(engine_boundaries[idx])
        ed.fixed(engine_fix_flags[idx])

    ed_bs_index, ed_bf_index = pf_bf_index, pf_bf_index + len(engine_dvs)

    # joint design variables
    # aircraft
    aircraft_mounting_dv_names = ['main wing coefficient x', 'main wing coefficient z', 'horizontal wing coefficient x',
                                  'horizontal wing coefficient z', 'vertical wing coefficient x',
                                  'vertical wing coefficient z']
    aircraft_mounting_boundaries = [[0, 1],
                                    [0, 1],
                                    [0, 1],
                                    [0, 1],
                                    [0, 1],
                                    [0, 1]]

    aircraft_mounting_dv_num = len(aircraft_mounting_dv_names)
    aircraft_mounting_fix_flags = [False for _ in range(aircraft_mounting_dv_num)]

    acmx = 0.4
    acmz = 0
    achx = 0.9
    achz = 0
    acbx = 0.9
    acbz = 0

    aircraft_mounting_dvs = [acmx, acmz, achx, achz, acbx, acbz]

    am_dv_sets = [DesignVariable(name) for name in aircraft_mounting_dv_names]

    for idx, amd in enumerate(am_dv_sets):
        amd.set_val(aircraft_mounting_dvs[idx])
        amd.set_bound(aircraft_mounting_boundaries[idx])
        amd.fixed(aircraft_mounting_fix_flags[idx])

    am_bs_index, am_bf_index = ed_bf_index, ed_bf_index + len(aircraft_mounting_dvs)

    # engine
    engine_mounting_dv_names = ['core engine mounting coefficient x', 'core engine mounting coefficient y',
                                'core engine moiunting turnover angle', 'core engine sign',
                                'distributed engine mounting coefficient x', 'distributed engine mounting coefficient y',
                                'distributed engine mounting turnover angle', 'distributed engine sign']
    engine_mounting_boundaries = [[0, 1],
                                  [0, 1],
                                  [0, 90],
                                  [-1, 1],
                                  [0, 1],
                                  [0, 1],
                                  [0, 90],
                                  [-1, 1]]

    engine_mounting_dv_num = len(engine_mounting_dv_names)
    engine_mounting_fix_flags = [False for _ in range(engine_mounting_dv_num)]

    ecmx = 0.1
    ecmy = 0.1
    theta_ec = 0
    sign_ec = -1
    edmx = 0.1
    edmy = 0.1
    theta_ed = 0
    sign_ed = 1

    engine_mounting_dvs = [ecmx, ecmy, theta_ec, sign_ec, edmx, edmy, theta_ed, sign_ed]

    em_dv_sets = [DesignVariable(name) for name in engine_mounting_dv_names]

    for idx, emd in enumerate(em_dv_sets):
        emd.set_val(engine_mounting_dvs[idx])
        emd.set_bound(engine_mounting_boundaries[idx])
        emd.fixed(engine_mounting_fix_flags[idx])

    em_bs_index, em_bf_index = am_bf_index, am_bf_index + len(engine_mounting_dvs)

    # BLI
    bli_dv_names = ['distortion angle']
    bli_boundaries = [[0, 120]]
    bli_dv_num = len(bli_dv_names)
    bli_fix_flags = [False for _ in range(bli_dv_num)]

    dist_ang = 60

    bli_dvs = [dist_ang]

    bli_dv_sets = [DesignVariable(name) for name in bli_dv_names]

    for idx, bld in enumerate(bli_dv_sets):
        bld.set_val(bli_dvs[idx])
        bld.set_bound(bli_boundaries[idx])
        bld.fixed(bli_fix_flags[idx])

    bl_bs_index, bl_bf_index = em_bf_index, em_bf_index + len(bli_dvs)

    # electric
    electric_dv_names = ['material level', 'battery electric density']
    electric_boundaries = [[0.1, 1.0], [5.2, 10.0]]

    electric_dv_num = len(electric_dv_names)
    electric_fix_flags = [False for _ in range(electric_dv_num)]

    mat_lev = 1.0
    bat_ele_dense = 5.2  # [kW/kg]
    electric_dvs = [mat_lev, bat_ele_dense]

    e_dv_sets = [DesignVariable(name) for name in electric_dv_names]

    for idx, ed in enumerate(e_dv_sets):
        ed.set_val(electric_dvs[idx])
        ed.set_bound(electric_boundaries[idx])
        ed.fixed(electric_fix_flags[idx])

    ele_bs_index, ele_bf_index = bl_bf_index, bl_bf_index + len(electric_dvs)

    # mission
    mission_dv_names = ['altitude', 'mach number', 'thrust at off design point', 'lift by drag', 'cruise range',
                        'max takeoff weight', 'passenger number', 'fuel coefficient', 'cargo weight', 'cargo volume']
    mission_boundaries = [[10000, 14000],
                          [0.7, 0.9],
                          [120000, 150000],
                          [15, 17],
                          [4500, 5000],
                          [75000, 80000],
                          [100, 200],
                          [0.4, 0.7],
                          [6000, 7000],
                          [30, 40]]

    mission_dv_num = len(mission_dv_names)
    mission_fix_flags = [False for _ in range(mission_dv_num)]

    altitude = 10668  # [m]
    mach_number = 0.82
    thrust_doff = 133000  # [N]
    ld = 17
    cruise_range = 4808  # [km]
    mtow = 78000  # [kg]
    passenger_num = 150
    fuel_coef = 0.6
    cargo_weight = 6300  # [kg]
    cargo_volume = 37.63  # [m^3]

    mission_dvs = [altitude, mach_number, thrust_doff, ld, cruise_range, mtow, passenger_num, fuel_coef, cargo_weight, cargo_volume]

    m_dv_sets = [DesignVariable(name) for name in mission_dv_names]

    for idx, md in enumerate(m_dv_sets):
        md.set_val(mission_dvs[idx])
        md.set_bound(mission_boundaries[idx])
        md.fixed(mission_fix_flags[idx])

    mis_bs_index, mis_bf_index = ele_bf_index, ele_bf_index + len(mission_dvs)
    









if __name__ == '__main__':
    main()

