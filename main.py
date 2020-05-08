"""
--Development for conceptual design and simulation for aircraft--


 **Aircraft**

    1. Fuel type
           'jet', 'electric', 'hybrid', 'hydrogen'

    2. Aircraft type
          'normal', 'Blended Wing Body', 'drone', 'Hyper sonic', 'propeller'

    3. Aircraft shape's components
          ['main wing', 'vertical wing', 'horizontal wing', 'engine', 'nacelle', 'winglet', 'cabin fuselage', 'cockpit fuselage', 'after cabin fuselage', 'leg']

    4. Aircraft Type and Component
        1. normal
                ['main wing', 'vertical wing', 'horizontal wing', 'engine', 'nacelle', 'winglet', 'cabin fuselage',
                'cockpit fuselage', 'after cabin fuselage', 'leg']

        2. BWB
                normal(without 'vertical wing' & 'horizontal wing') + different shape definition

        3. drone(UAV)
                ['main wing', 'engine', 'propeller', 'cockpit fuselage', 'cabin fuselage']

        4. Hyper sonic
                normal(without 'horizontal wing') + different wing shape + different aerodynamic performance modules

        5. propeller
                normal + different shape definition

    5. wing type(airfoil)
         cross section(NACA 6), horizontal section(Trapezoid,Delta,Diamond,rectangle)

**Engine**

    1. Engine type
         'turbojet', 'turbofan', 'turboprop'(propeller),'turboelectric', 'partialelectric', 'allelectric', 'serieshybrid', 'partialhybrid', 'parallelhybrid'

         optional engine version: BLI(Boundary Layer Ingestion)

    2. Engine components
        1. electric fan
               [inlet, fan, nozzle, jet]

        2. turbofan
               [inlet, lpc, hpc, cc, hpt, hptcool, lpt, lptcool, coreout, nozzle, jet, fan, fannozzle, fanjet]

        3. turbojet
               [inlet, lpc, hpc, cc, hpt, hptcool, lpt, lptcool, coreout, nozzle, jet]

        4. turboprop(propeller)
               [inlet, lpc, hpc, cc, hot, hptcool, lpt, lptcool, coreout, nozzle, jet]

        5. turboelectric
               concept => (turboshaft => electric fan)

               [core: inlet, lpc, hpc, cc, hpt, hptcool, lpt, lptcool, coreout, nozzle, jet,
               electric fan: eleinlet, elefan, elenozzle, elejet]

        6. partialelectric
               concept (turbofan => electric fan)

               [core: inlet, lpc, hpc, cc, hpt, hptcool, lpt, lptcool, coreout, nozzle, jet, fan, fannozzle, fanjet,
               electric fan: eleinlet, elefan, elenozzle, elejet]

        7. allelectric
               [eleinlet, elefan, elenozzle, elejet] + [battery](electricity, fuel cell etc)

        8. serieshybrid
               concept => (turboshaft + battery => electric fan)

               [core: inlet, lpc, hpc, cc, hpt, hptcool, lpt, lptcool, coreout, nozzle, jet,
               [battery], electric fan: eleinlet, elefan, elenozzle, elejet]

        9. partialhybrid
               concept => (turbofan + battery => electric fan)
               [core: inlet, lpc, hpc, cc, hpt, hptcool, lpt, lptcool, coreout, nozzle, jet,
               [battery], electric fan: eleinlet, elefan, elenozzle, elejet]

        10. parallel hybrid
               concept => (battery => turbofan)
               [core: inlet, lpc, hpc, cc, hpt, hptcool, lpt, lptcool, coreout, nozzle, jet, fan, fannozzle, fanjet], [battery]


**Initial parameters**

     aircraft shape parameters + aircraft configuration parameters + aircraft aerodynamic parameters + engine parameters + engine configuration parameters

     1. Aircraft shape parameters
             Main wing
                (wing width, wing thickness, the ratio of thickness and wing span, aspect ratio)

             Vertical wing
                 (wing width, wing thickness, the ratio of thickness and wing span, aspect ratio)

             Horizontal wing
                 (wing width, wing thickness, the ratio of thickness and wing span, aspect ratio)}

             Fuselage shape
                 {'cabin':(length, width), 'cockpit': (length, width), 'after cabin': (length, width)}

             Nacelle
                 include engine components parameters

     2. Aircraft configuration parameters
             1. wing mounting positions
                  3D coordinates (x, y, z)

             2. engine mounting positions
                  3D coordinates (x, y, z)

             3. aircraft other required args
                  aircraft weight model

             4. passenger number
                  the number of boarding

             5. cargo weight
                  the weight of total cargo


             6. cruise altitude
                  the height at cruise point

             7. cruise mach
                  the mach number at cruise point


# 3. aircraft aerodynamic parameters
#    L/D(?), AOA(attack of angle)
# 4. engine parameters
#    BPR(bypass ratio), FPR(fan pressure ratio), OPR(overall pressure ratio), TIT(turbine inlet temperature),
#    BPRe(bypass ratio for electric), FPRe(fan pressure ratio for electric), Nfan(the number of electric fan),
#    electric efficiency, the ratio of electric power and engine generating power(?), engine component efficiency,
#    BLI parameters
# 5. engine configuration parameters
#    the number of engine, thrust of engine at design point, thrust of engine at off design point,
#    engine material quality, each stage number of compressor or turbine


# the definition of flight path
# 0. warming up => 1. takeoff => 2. climb => 3. cruise => 4. descend(+ loiter) => 5. landing => 6. stop


# fundamental equation
# Breguet formula
# propeller: Range = (propeller efficient / bp ) * (L / D) * ln(W init / W finish), bp => m fuel[N] / propeller Power[W] / s
# jet engine: Range = (jet velocity / SFC) * (L/D) * ln(W init / W finish), SFC => m fuel[N] / T[N] / s


# poll of coding
# write design variables into csv file or generate the sets of the design variables at random value

# DataBase
# operate database by pandas
# aircraft.csv
# format
#        a1 a2 a3 .... an  <= parameters name
# aname   1  2  3       5
# bname   1  2  3       5
# engine.csv
#        a1 a2 a3 .... an  <= parameters name
# aname   1  2  3       5
# bname   1  2  3       5


# Module
# Physic class() (physics.py)=> to compute the value of physics(ex. density, Pressure, Temperature,...)
# Design variables controller class() => to assign design variables into each class and adjust the interaction of design variables
# Mission class() => define the mission
# Aircraft parameters class() => to keep the aircraft parameters
#          return params => numpy array  * Initialize 0 array
# Aircraft performance class() => compute aerodynamic performance and weight
#    aircraft aerodynamic performance class() => calculate L/D at cruise
#    aircraft weight class() => calculate overall weight
#           return weight results => numpy array   * Initialize 0 array
#           component class()
# Engine parameters class() => to keep the engine parameters
#          return params => numpy array   * Initialize 0 array
# Engine performance class() => compute thermodynamic performance and weight
#    engine thermodynamic class() => calculate SFC and Thrust at cruise and takeoff
#        design point class()
#           return thermodynamic results at design point => numpy array
#        off design point class()
#           return thermodynamic results at off design point => numpy array
#    engine weight class() => calculate engine weight(core weight, electric fan weight, electricity weight)
#        core weight class()
#           return core weight results => numpy array  * Initialize 0 array
#        electric fan weight class()
#           return electric fan weight results => numpy array  * Initialize 0 array
#        electricity weight class() => (battery weight, fuel cell weight, biological fuel weight)
#           return electricity weight => numpy array  * Initialize 0 array
#            component class()
# Aircraft view class() => to plot the aircraft's view based on the given parameters
# Baseline Estimation class() => define the scale factor for aircraft design(from public value)
# DataBase manage class() => manage the database values


# Optimization module
# Gradient descent class() -> main function: class object.optimize()
# Evolutionary Algorithm class()
#     NSGA2() -> main function: class object.optimize()
#     PSO() -> main function: class object.optimize()
#     CMAES() -> main function: class object.optimize()


# Analysis module
# plot contour
# plot result by jupyter notebook


# Self driving module


# UseCase for IAEA
# Implementation of aircraft design
# 0. tuning the baseline model
# 1. input design variables
# 2. calculate the objective function
# 3. plot the shape parameters at plotter library and save them(csv file)


# Implementation of optimization of aircraft design
# 0. tuning the baseline model
# 1. decide the optimization method
# 2. optimize the objective function
# 3. get the optimal solution and save them
# 4. plot the shape parameters


# Implementation of aircraft simulation
# 0. set the optimal design variables
# 1. construct 2D aircraft
# 2. set the city obstacle or landmark
# 3. apply RL(Reinforcement Learning) or SLAM(Simultaneous Localization and Mapping) in order to find the better path
# 4. plot the explored path at graph
"""




