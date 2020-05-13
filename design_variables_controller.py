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
        # create dictionary combined with name and index number
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

        # create dictionary combined with name and index number
        self.aircraft_wing_dv_idx_dict = {}
        for idx, name in enumerate(self.aircraft_wing_dv_names):
            self.aircraft_wing_dv_idx_dict[name] = idx

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

        # Initialize aircraft wing dv sets
        self.aw_dv_sets = [DesignVariable(name) for name in self.aircraft_wing_dv_names]

    def set_bounds(self, name, bounds):
        """
        replace boundary condition

        :param name: str
                     design variable name
        :param bounds: list
                       list which contains minimum and maximum value
        :return: None
        """
        idx = self.aircraft_wing_dv_idx_dict[name]
        self.aircraft_wing_boundaries[idx] = bounds

    def set_fix(self, name, flag=True):
        """
        decide how to cope with each design variable

        :param name: str
                     design variable name
        :param flag: Boolean
                     flag which indicates whether or not design variable is fixed
        :return: None
        """
        idx = self.aircraft_wing_dv_idx_dict[name]
        self.aircraft_wing_fix_flags[idx] = flag

    def create_dv_sets(self, aircraft_wing_dvs):
        """
        create design variable sets

        :param aircraft_wing_dvs: list
                                  list which has the sets of design variable value
        :return: None
        """

        # set aircraft wing dv sets
        for idx, ad in enumerate(self.aw_dv_sets):
            ad.set_val(aircraft_wing_dvs[idx])
            ad.set_bound(self.aircraft_wing_boundaries[idx])
            ad.fixed(self.aircraft_wing_fix_flags[idx])

# Aircraft performance design variable class
class AircraftPerformanceDesignVariable(object):

    def __init__(self):
        self.aircraft_performance_dv_names = ['attack of angle']
        self.aircraft_performance_dv_idx_dict = {}
        for idx, name in enumerate(self.aircraft_performance_dv_names):
            self.aircraft_performance_dv_idx_dict[name] = idx
        self.aircraft_performance_boundaries = [[0, 6]]
        self.aircraft_performance_dv_num = len(self.aircraft_performance_dv_names)
        self.aircraft_performance_fix_flags = [False for _ in range(self.aircraft_performance_dv_num)]

        # Initialize the aircraft performance dv sets
        self.ap_dv_sets = [DesignVariable(name) for name in self.aircraft_performance_dv_names]

    def set_bounds(self, name, bounds):
        """
        replace boundary condition

        :param name: str
                     design variable name
        :param bounds: list
                       list which contains minimum and maximum value
        :return: None
        """
        idx = self.aircraft_performance_dv_idx_dict[name]
        self.aircraft_performance_boundaries[idx] = bounds

    def set_fix(self, name, flag=True):
        """
        decide how to cope with each design variable

        :param name: str
                     design variable name
        :param flag: Boolean
                     flag which indicates whether or not design variable is fixed
        :return: None
        """
        idx = self.aircraft_performance_dv_idx_dict[name]
        self.aircraft_performance_fix_flags[idx] = flag

    def create_dv_sets(self, aircraft_performance_dvs):
        """
        create design variable sets

        :param aircraft_wing_dvs: list
                                  list which has the sets of design variable value
        :return: None
        """

        # set aircraft wing dv sets
        for idx, ad in enumerate(self.ap_dv_sets):
            ad.set_val(aircraft_performance_dvs[idx])
            ad.set_bound(self.aircraft_performance_boundaries[idx])
            ad.fixed(self.aircraft_performance_fix_flags[idx])


# Engine design variable class
class EngineDesignVariable(object):

    def __init__(self):
        self.engine_dv_names = ['OPR', 'TIT', 'BPR', 'FPR', 'Nen', 'technical level', 'cool air lpt rate',
                           'cool air hpt rate',
                           'engine material quality', 'fan stage number', 'lpc stage number', 'hpc stage number',
                           'hpt stage number', 'lpt stage number', 'fan load factor', 'lpc load factor',
                           'hpc load factor',
                           'hpt load factor', 'lpt load factor', 'BPRe', 'FPRe', 'Nfan', 'engine electric efficiency',
                           'engine electric density']

        self.engine_dv_idx_dict = {}

        for idx, name in enumerate(self.engine_dv_names):
            self.engine_dv_idx_dict[name] = idx

        self.engine_boundaries = [[20, 40],  # OPR
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

        self.engine_dv_num = len(self.engine_dv_names)

        self.engine_fix_flags = [False for _ in range(self.engine_dv_num)]

        self.e_dv_sets = [DesignVariable(name) for name in self.engine_dv_names]

    def set_bounds(self, name, bounds):
        """
        replace boundary condition

        :param name: str
                     design variable name
        :param bounds: list
                       list which contains minimum and maximum value
        :return: None
        """
        idx = self.engine_dv_idx_dict[name]
        self.engine_boundaries[idx] = bounds

    def set_fix(self, name, flag=True):
        """
        decide how to cope with design variable

        :param name: str
                     design variable name
        :param flag: boolean
                     flag which indicates whether or not design variable is fixed
        :return: None
        """
        idx = self.engine_dv_idx_dict[name]
        self.engine_fix_flags[idx] = flag

    def create_dv_sets(self, engine_dvs):
        """
        create design variable sets

        :param engine_dvs: list
                           the set of engine design variable's value
        :return: None
        """
        for idx, ed in enumerate(self.e_dv_sets):
            ed.set_val(engine_dvs[idx])
            ed.set_bound(self.engine_boundaries[idx])
            ed.fixed(self.engine_fix_flags[idx])


# Joint Aircraft design variable class
class JointAircraftDesignVariable(object):

    def __init__(self):
        self.aircraft_mounting_dv_names = ['main wing coefficient x', 'main wing coefficient z',
                                      'horizontal wing coefficient x',
                                      'horizontal wing coefficient z', 'vertical wing coefficient x',
                                      'vertical wing coefficient z']

        self.aircraft_mounting_dv_idx_dict = {}

        for idx, name in enumerate(self.aircraft_mounting_dv_names):
            self.aircraft_mounting_dv_idx_dict[name] = idx

        self.aircraft_mounting_boundaries = [[0, 1],
                                        [0, 1],
                                        [0, 1],
                                        [0, 1],
                                        [0, 1],
                                        [0, 1]]

        self.aircraft_mounting_dv_num = len(self.aircraft_mounting_dv_names)
        self.aircraft_mounting_fix_flags = [False for _ in range(self.aircraft_mounting_dv_num)]

        self.am_dv_sets = [DesignVariable(name) for name in self.aircraft_mounting_dv_names]

    def set_bounds(self, name, bounds):
        """
        replace boundary condition

        :param name: str
                     design variable name
        :param bounds: list
                       list which contains minimum and maximum value
        :return: None
        """
        idx = self.aircraft_mounting_dv_idx_dict[name]
        self.aircraft_mounting_boundaries[idx] = bounds

    def set_fix(self, name, flag=True):
        """
        decide how to cope with design variable

        :param name: str
                     design variable name
        :param flag: boolean
                     flag which indicates whether or not design variable is fixed
        :return: None
        """
        idx = self.aircraft_mounting_dv_idx_dict[name]
        self.aircraft_mounting_fix_flags[idx] = flag

    def create_dv_sets(self, aircraft_mounting_dvs):
        """
        create design variable sets

        :param aircraft_mounting_dvs: list
                           the set of engine design variable's value
        :return: None
        """

        for idx, amd in enumerate(self.am_dv_sets):
            amd.set_val(aircraft_mounting_dvs[idx])
            amd.set_bound(self.aircraft_mounting_boundaries[idx])
            amd.fixed(self.aircraft_mounting_fix_flags[idx])



# Joint Engine design variable class
class JointEngineDesignVariable(object):

    def __init__(self):
        self.engine_mounting_dv_names = ['core engine mounting coefficient x', 'core engine mounting coefficient y',
                                    'core engine moiunting turnover angle', 'core engine sign',
                                    'distributed engine mounting coefficient x',
                                    'distributed engine mounting coefficient y',
                                    'distributed engine mounting turnover angle', 'distributed engine sign']

        self.engine_mounting_dv_idx_dict = {}

        for idx, name in enumerate(self.engine_mounting_dv_names):
            self.engine_mounting_dv_idx_dict[name] = idx

        self.engine_mounting_boundaries = [[0, 1],
                                      [0, 1],
                                      [0, 90],
                                      [-1, 1],
                                      [0, 1],
                                      [0, 1],
                                      [0, 90],
                                      [-1, 1]]

        self.engine_mounting_dv_num = len(self.engine_mounting_dv_names)
        self.engine_mounting_fix_flags = [False for _ in range(self.engine_mounting_dv_num)]

        self.em_dv_sets = [DesignVariable(name) for name in self.engine_mounting_dv_names]

    def set_bounds(self, name, bounds):
        """
        replace boundary condition

        :param name: str
                     design variable name
        :param bounds: list
                       list which contains minimum and maximum value
        :return: None
        """
        idx = self.engine_mounting_dv_idx_dict[name]
        self.engine_mounting_boundaries[idx] = bounds

    def set_fix(self, name, flag=True):
        """
        decide how to cope with design variable

        :param name: str
                     design variable name
        :param flag: boolean
                     flag which indicates whether or not design variable is fixed
        :return: None
        """
        idx = self.engine_mounting_dv_idx_dict[name]
        self.engine_mounting_fix_flags[idx] = flag

    def create_dv_sets(self, engine_mounting_dvs):
        """
        create design variable sets

        :param engine_mounting_dvs: list
                                    the sets of design variable value
        :return: None
        """

        for idx, emd in enumerate(self.em_dv_sets):
            emd.set_val(engine_mounting_dvs[idx])
            emd.set_bound(self.engine_mounting_boundaries[idx])
            emd.fixed(self.engine_mounting_fix_flags[idx])

# Electric design variable class
class ElectricDesignVariable(object):

    def __init__(self):
        self.electric_dv_names = ['material level', 'battery electric density']

        self.electric_dv_idx_dict = {}

        for idx, name in enumerate(self.electric_dv_names):
            self.electric_dv_idx_dict[name] = idx

        self.electric_boundaries = [[0.1, 1.0], [5.2, 10.0]]

        self.electric_dv_num = len(self.electric_dv_names)
        self.electric_fix_flags = [False for _ in range(self.electric_dv_num)]

        self.e_dv_sets = [DesignVariable(name) for name in self.electric_dv_names]

    def set_bounds(self, name, bounds):
        """
        replace boundary condition

        :param name: str
                     design variable name
        :param bounds: list
                       list which contains minimum and maximum value
        :return: None
        """
        idx = self.electric_dv_idx_dict[name]
        self.electric_boundaries[idx] = bounds

    def set_fix(self, name, flag=True):
        """
        decide how to cope with design variable

        :param name: str
                     design variable name
        :param flag: boolean
                     flag which indicates whether or not design variable is fixed
        :return: None
        """
        idx = self.electric_dv_idx_dict[name]
        self.electric_fix_flags[idx] = flag

    def create_dv_sets(self, electric_dvs):
        """
        create design variable sets

        :param electric_dvs: list
                             the sets of design variable value
        :return: None
        """
        for idx, ed in enumerate(self.e_dv_sets):
            ed.set_val(electric_dvs[idx])
            ed.set_bound(self.electric_boundaries[idx])
            ed.fixed(self.electric_fix_flags[idx])


# BLI design variable class
class BLIDesignVariable(object):

    def __init__(self):
        self.bli_dv_names = ['distortion angle']
        self.bli_dv_idx_dict = {}

        for idx, name in enumerate(self.bli_dv_names):
            self.bli_dv_idx_dict[name] = idx

        self.bli_boundaries = [[0, 120]]
        self.bli_dv_num = len(self.bli_dv_names)
        self.bli_fix_flags = [False for _ in range(self.bli_dv_num)]

        self.bli_dv_sets = [DesignVariable(name) for name in self.bli_dv_names]

    def set_bounds(self, name, bounds):
        """
        replace boundary condition

        :param name: str
                     design variable name
        :param bounds: list
                       list which contains minimum and maximum value
        :return: None
        """
        idx = self.bli_dv_idx_dict[name]
        self.bli_boundaries[idx] = bounds

    def set_fix(self, name, flag=True):
        """
        decide how to cope with design variable

        :param name: str
                     design variable name
        :param flag: boolean
                     flag which indicates whether or not design variable is fixed
        :return: None
        """
        idx = self.bli_dv_idx_dict[name]
        self.bli_fix_flags[idx] = flag

    def create_dv_sets(self, bli_dvs):
        """
        create design variable sets

        :param bli_dvs: list
                        the sets of design variable value
        :return: None
        """
        for idx, bld in enumerate(self.bli_dv_sets):
            bld.set_val(bli_dvs[idx])
            bld.set_bound(self.bli_boundaries[idx])
            bld.fixed(self.bli_fix_flags[idx])


# Mission design variable class
class MissionDesignVariable(object):

    def __init__(self):
        self.mission_dv_names = ['altitude', 'mach number', 'thrust at off design point', 'lift by drag', 'cruise range',
                            'max takeoff weight', 'passenger number', 'fuel coefficient', 'cargo weight',
                            'cargo volume']

        self.mission_dv_idx_dict = {}

        for idx, name in enumerate(self.mission_dv_names):
            self.mission_dv_idx_dict[name] = idx

        self.mission_boundaries = [[10000, 14000],
                              [0.7, 0.9],
                              [120000, 150000],
                              [15, 17],
                              [4500, 5000],
                              [75000, 80000],
                              [100, 200],
                              [0.4, 0.7],
                              [6000, 7000],
                              [30, 40]]

        self.mission_dv_num = len(self.mission_dv_names)
        self.mission_fix_flags = [False for _ in range(self.mission_dv_num)]

        self.m_dv_sets = [DesignVariable(name) for name in self.mission_dv_names]

    def set_bounds(self, name, bounds):
        """
        replace boundary condition

        :param name: str
                     design variable name
        :param bounds: list
                       list which contains minimum and maximum value
        :return: None
        """
        idx = self.mission_dv_idx_dict[name]
        self.mission_boundaries[idx] = bounds

    def set_fix(self, name, flag=True):
        """
        decide how to cope with design variable

        :param name: str
                     design variable name
        :param flag: boolean
                     flag which indicates whether or not design variable is fixed
        :return: None
        """
        idx = self.mission_dv_idx_dict[name]
        self.mission_fix_flags[idx] = flag

    def create_dv_sets(self, mission_dvs):
        """
        create design variable sets

        :param mission_dvs: list
                            the sets of design variable value
        :return: None
        """
        for idx, md in enumerate(self.m_dv_sets):
            md.set_val(mission_dvs[idx])
            md.set_bound(self.mission_boundaries[idx])
            md.fixed(self.mission_fix_flags[idx])



# Integration Design Variables Controller
class DesignVariablesController(object):

    def __init__(self, aircraft_params_class, engine_params_class):

        # Parameter class
        self.aircraft_params_class = aircraft_params_class
        self.engine_params_class = engine_params_class

        # start index(s_idx) and final index(f_idx) for each design variables
        # fuselage
        self.fl_s_idx = 0
        self.fl_f_idx = 0
        # wing
        self.wi_s_idx = 0
        self.wi_f_idx = 0
        # performance
        self.pf_s_idx = 0
        self.pf_f_idx = 0
        # engine
        self.e_s_idx = 0
        self.e_f_idx = 0
        # joint aircraft
        self.ja_s_idx = 0
        self.ja_f_idx = 0
        # join engine
        self.je_s_idx = 0
        self.je_f_idx = 0
        # BLI
        self.bli_s_idx = 0
        self.bli_f_idx = 0
        # mission
        self.ms_s_idx = 0
        self.ms_f_idx = 0


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

    # Initialization
    awdv = AircraftWingDesignVariable()
    awdv.create_dv_sets(aircraft_wing_dvs)

    # confirmation
    print('')
    print('aircraft wing class')
    for u in awdv.aw_dv_sets:
        print(u.val)
        print(u.bound)
        print(u.fix)
    print('')

    # build aircraft performance design variable class
    aoa = 4  # attack of angle
    aircraft_performance_dvs = [aoa]

    # Initialization
    apdv = AircraftPerformanceDesignVariable()
    apdv.create_dv_sets(aircraft_performance_dvs)

    # confirmation
    print('')
    print('aircraft performance class')
    for u in apdv.ap_dv_sets:
        print(u.val)
        print(u.bound)
        print(u.fix)
    print('')

    # build engine design variable class
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

    # Initialization
    edv = EngineDesignVariable()
    edv.create_dv_sets(engine_dvs)

    # confirmation
    print('')
    print('engine class')
    for u in edv.e_dv_sets:
        print(u.val)
        print(u.bound)
        print(u.fix)
    print('')

    # build joint aircraft design variable class
    acmx = 0.4
    acmz = 0
    achx = 0.9
    achz = 0
    acbx = 0.9
    acbz = 0

    aircraft_mounting_dvs = [acmx, acmz, achx, achz, acbx, acbz]

    # Initialization
    jadv = JointAircraftDesignVariable()
    jadv.create_dv_sets(aircraft_mounting_dvs)

    print('')
    print('Joint aircraft class')
    for u in jadv.am_dv_sets:
        print(u.val)
        print(u.bound)
        print(u.fix)
    print('')

    # build joint engine design variable class
    ecmx = 0.1
    ecmy = 0.1
    theta_ec = 0
    sign_ec = -1
    edmx = 0.1
    edmy = 0.1
    theta_ed = 0
    sign_ed = 1

    engine_mounting_dvs = [ecmx, ecmy, theta_ec, sign_ec, edmx, edmy, theta_ed, sign_ed]

    # Initialization
    jedv = JointEngineDesignVariable()
    jedv.create_dv_sets(engine_mounting_dvs)

    print('')
    print('Joint engine class')
    for u in jedv.em_dv_sets:
        print(u.val)
        print(u.bound)
        print(u.fix)
    print('')

    # build electric design variable class
    mat_lev = 1.0
    bat_ele_dense = 5.2  # [kW/kg]
    electric_dvs = [mat_lev, bat_ele_dense]

    eldv = ElectricDesignVariable()
    eldv.create_dv_sets(electric_dvs)

    print('')
    print('Electric class')
    for u in eldv.e_dv_sets:
        print(u.val)
        print(u.bound)
        print(u.fix)
    print('')

    # build BLI design variable class
    dist_ang = 60

    bli_dvs = [dist_ang]

    blidv = BLIDesignVariable()
    blidv.create_dv_sets(bli_dvs)

    print('')
    print('BLI class')
    for u in blidv.bli_dv_sets:
        print(u.val)
        print(u.bound)
        print(u.fix)
    print('')

    # build mission design variable class
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

    mission_dvs = [altitude, mach_number, thrust_doff, ld, cruise_range, mtow, passenger_num, fuel_coef, cargo_weight,
                   cargo_volume]

    mdv = MissionDesignVariable()
    mdv.create_dv_sets(mission_dvs)

    print('')
    print('Mission class')
    for u in mdv.m_dv_sets:
        print(u.val)
        print(u.bound)
        print(u.fix)
    print('')




if __name__ == '__main__':
    main()

