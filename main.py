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
               [inlet, lpc, hpc, cc, hpt, hptcool, lpt, lptcool, coreout, nozzle, jet, fan, fan_nozzle, fan_jet]

        3. turbojet
               [inlet, lpc, hpc, cc, hpt, hptcool, lpt, lptcool, coreout, nozzle, jet]

        4. turboprop(propeller)
               [inlet, lpc, hpc, cc, hot, hptcool, lpt, lptcool, coreout, nozzle, jet]

        5. turboelectric
               concept => (turboshaft => electric fan)

               [core: inlet, lpc, hpc, cc, hpt, hptcool, lpt, lptcool, coreout, nozzle, jet,
               electric fan: fan_electric_inlet, fan_electric, fan_electric_nozzle, fan_electric_jet]

        6. partialelectric
               concept (turbofan => electric fan)

               [core: inlet, lpc, hpc, cc, hpt, hptcool, lpt, lptcool, coreout, nozzle, jet, fan, fan_nozzle, fan_jet,
               electric fan: fan_electric_inlet, fan_electric, fan_electric_nozzle, fan_electric_jet]

        7. allelectric
               [fan_electric_inlet, fan_electric, fan_electric_nozzle, fan_electric_jet] +
               [battery](electricity, fuel cell etc)

        8. serieshybrid
               concept => (turboshaft + battery => electric fan)

               [core: inlet, lpc, hpc, cc, hpt, hptcool, lpt, lptcool, coreout, nozzle, jet,
               [battery], electric fan: fan_electric_inlet, fan_electric, fan_electric_nozzle, fan_electric_jet]

        9. partialhybrid
               concept => (turbofan + battery => electric fan)
               [core: inlet, lpc, hpc, cc, hpt, hptcool, lpt, lptcool, coreout, nozzle, jet,
               [battery], electric fan: eleinlet, elefan, elenozzle, elejet]

        10. parallel hybrid
               concept => (battery => turbofan)
               [core: inlet, lpc, hpc, cc, hpt, hptcool, lpt, lptcool, coreout, nozzle, jet, fan, fan_nozzle, fan_jet],
               [battery]


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

     3. Aircraft aerodynamic parameters
         L/D(?)

         AOA(attack of angle)

     4. engine parameters
         BPR
            bypass ratio, the ratio of core airflow and fan airflow

         FPR
            fan pressure ratio, the ratio of inlet fan pressure and outlet fan pressure

         OPR
            overall pressure ratio, the ratio inlet compressor and outlet compressor

         TIT
            turbine inlet temperature, the temperature of turbine entrance

         BPRe
            bypass ratio for electric fan, the ratio of core airflow and distributed fan airflow

         FPRe
            fan pressure ratio for electric fan, the ratio of inlet fan pressure and outlet fan pressure

         Nfan
            the number of electric fan

         electric efficiency
            the efficiency of converting heat power generated by jet engine into electricity

         the ratio of electric power and engine generating power
            the distributed ratio for supplementing the current power

         engine component efficiency
            the heat efficiency which each engine component has

         BLI parameters
            the relational variables with Boundary Ingestion Layer

     5. engine configuration parameters
         Nen
           the number of engine

         thrust_design_point
           thrust of engine at design point

         thrust_off_design_point
           thrust of engine at off design point

         quality_engine
           engine material quality

         Nlx
           stage number of each compressor or turbine

         LFx
           stage load factor of each compressor or turbine

         cool_airx
           the distribution of cool air for high and low pressure turbine




**The definition of flight path**

0. warming up => 1. takeoff => 2. climb => 3. cruise => 4. descend(+ loiter) => 5. landing => 6. stop




**Fundamental equation**

Breguet formula
     1.propeller
        Range = (propeller efficient / bp ) * (L / D) * ln(W init / W finish), bp => m fuel[N] / propeller Power[W] / s

     2.jet engine
        Range = (jet velocity / SFC) * (L/D) * ln(W init / W finish), SFC => m fuel[N] / T[N] / s


**Poll of coding**

write design variables into csv file or generate the sets of the design variables at random value


**Module**

Physic class(physics.py)
      to compute the value of physics(ex. density, Pressure, Temperature,...)

Design variables controller class(design_variables_controller.py)
    to assign design variables into each class and adjust the interaction of design variables

Mission class(define_mission.py)
    to define the mission

Aircraft parameters class(aircraft_params.py)
    to keep the aircraft parameters

    return params => numpy array  * Initialize 0 array


Aircraft performance class(aircraft_performance.py)
    to compute aerodynamic performance and weight

    aircraft aerodynamic performance class(aerodynamic_performance.py)
      calculate L/D at cruise

    aircraft weight class(aircraft_weight.py)
      calculate overall weight
      return weight results => numpy array   * Initialize 0 array

    special aircraft shape class()
      Drone class(drone.py)

      Blended Wing Body class(bwb.py)

      Hyper sonic class(hyper_sonic.py)

      Propeller class(propeller.py)



    component class(aircraft_component.py)
        base component class format()
           __init__(aircraft_params_class)
            weight = 0

            aircraft_params_class

            (needed?)

            (x, y, z) => list

            (join equipment index) => list

           run()()
             feedforward()

             return None


        1: MainWing class()
           keep the main wing weight or params and calculate weight

        2: Horizontal tail()
           keep the horizontal tail wing weight or params and calculate weight

        3: Vertical tail()
           keep the vertical tail wing weight or params and calculate weight

        4: Fuselage()
           keep the fuselage weight or params and calculate weight

        5: Main Landing Gear()
           keep the main landing gear's weight or params and calculate weight

        6: Nose landing Gear()
           keep the nose landing gear's weight or params and calculate weight

        7: Nacelle()
           keep the nacelle's weight or params and calculate weight

        8: Engine Control()
           keep the engine controller's weight or params and calculate weight

        9: Starter()
           keep the starter's weight or params and calculate weight

        10: Fuel System()
           keep the fuel system's weight or params and calculate weight

        11: Flight Control()
           keep the flight controller's weight or params and calculate weight

        12: APU()
           keep the APU weight or params and calculate weight

        13: Instrument()
           keep the instrument's weight or params and calculate weight

        14: Hydraulics()
           keep the hydraulics's weight or params and calculate weight

        15: Electric()
           keep the electricity weight or params and calculate weight
           (maybe this class is not needed for electric aircraft)

        16: Avionic()
           keep the avionic's weight or params and calculate weight

        17: furnishing()
           keep the furnishing's weight or params and calculate weight

        18: Airconditioner()
           keep the air conditioner's weight or params and calculate weight

        19: Anti ice()
           keep the anti ice's weight or params and calculate weight

        20: Handling Gear()
           keep the handling gear's weight or params and calculate weight

        21: Engine()
           keep the engine weight but this class is not needed and designated
           engine_weight_class().result

        22: Passenger Equip()
           keep the main passenger equipment's weight or params and calculate weight



Engine parameters class(engine_params.py)
    to keep the engine parameters
    return params => numpy array   * Initialize 0 array

Engine performance class(engine_performance.py)
   to compute thermodynamic performance and weight

   engine thermodynamic class(engine_thermodynamic.py)
      calculate SFC and Thrust at cruise and takeoff

      design point class(engine_design_point.py)
          return thermodynamic results at design point => numpy array

      component class(engine_component_design_point.py)
         base component class()
           __init__()
             efficiency: type(numpy array or list(vector))

             component coefficient: type(numpy array or list(vector))

             previous physical value(Pressure, Temperature, density, pressure ratio, temperature ratio etc): type(numpy array or list(vector))

             current physical value: type(numpy array or list(vector))

           run()
             feedforward(calculate current physical value)

             save the result at current component

             return None

         0:Inlet()
            calculate physical value at inlet

         10:Fan()
            calculate physical value at fan

         20:LPC()
            calculate physical value at lpc

         25:HPC()
            calculate physical value at hpc

         30:CC()
            calculate physical value at cc

         40:HPT()
            calculate physical value at hpt

         41:HPTCool()
            calculate physical value at hptcool

         45:LPT()
            calculate physical value at lpt

         46:LPTCool()
            calculate physical value at lptcool

         50:CoreOut()
            calculate physical value at core outlet

         70:AfterBurner()
            calculate physical value at after burner

         80:Nozzle()
            calculate physical value at nozzle

         90:Jet()
            calculate physical value at jet

         18:FanNozzle()
            calculate physical value at fan nozzle

         19:FanJet()
            calculate physical value at fan jet

         100:FanElectricInlet()
            calculate physical value at electric fan inlet

         110:FanElectric()
            calculate physical value at electric fan

         118:FanElectricNozzle()
            calculate physical value at electric fan nozzle

         119:FanElectricJet()
            calculate physical value at electric jet



      off design point class(engine_off_design_point.py)
          return thermodynamic results at off design point => numpy array

        component class(engine_component_design_point.py)
          0:Inlet()
          10:Fan()
          20:LPC()
          25:HPC()
          30:CC()
          40:HPT()
          41:HPTCool()
          45:LPT()
          46:LPTCool()
          50:CoreOut()
          70:AfterBurner()
          80:Nozzle()
          90:Jet()
          18:FanNozzle()
          19:FanJet()
          100:FanElectricInlet()
          110:FanElectric()
          118:FanElectricNozzle()
          119:FanElectricJet()

   engine weight class(engine_weight.py)
      calculate engine weight(core weight, electric fan weight, electricity weight)

      core weight class(core_engine_weight.py)
          return core weight results => numpy array  * Initialize 0 array

      electric fan weight class(electric_fan_weight.py)
          return electric fan weight results => numpy array  * Initialize 0 array

      electricity weight class(electricity_weight.py)
          special fuel engine class()
            battery class()

            fuel cell class()

            biological fuel class()

          return electricity weight => numpy array  * Initialize 0 array

      component class()

Aircraft view class(view_aircraft.py)
     to plot the aircraft's view based on the given parameters

Baseline Estimation class(estimate_baseline.py)
     to define the scale factor for aircraft design(from public value)

DataBase manage class(DataBase/database_driven.py)
     to manage the database values


**Optimization module**

Gradient descent class()
   main function: class object.optimize()

Evolutionary Algorithm class()
      NSGA2()
        Non dominated sort Genetic Algorithm

        main function: class object.optimize()

      PSO()
        Partial Swarm Optimization

        main function: class object.optimize()

      CMAES()
        Covariance Matrix Adaptation Evolution Strategy
        main function: class object.optimize()


**Analysis module**

    plot contour

    plot result by jupyter notebook


**Self driving module**

    1.construct the aircraft or drone

    2.SLAM or Reinforcement Learning


**UseCase for IAEA**

Implementation of aircraft design
  0. tuning the baseline model

  1. input design variables

  2. calculate the objective function

  3. plot the shape parameters at plotter library and save them(csv file)


Implementation of optimization of aircraft design
  0. tuning the baseline model

  1. decide the optimization method

  2. optimize the objective function

  3. get the optimal solution and save them

  4. plot the shape parameters


Implementation of aircraft simulation
  0. set the optimal design variables

  1. construct 2D aircraft

  2. set the city obstacle or landmark

  3. apply RL(Reinforcement Learning) or SLAM(Simultaneous Localization and Mapping) in order to find the better path

  4. plot the explored path at graph

"""




