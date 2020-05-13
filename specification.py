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

             8. fuel coefficient
                  where to conduct the estimation of performance of aircraft at design point

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

         electric density:
            the density for electricity, unit is kW/kg or kg/kw

         electric efficiency
            the efficiency of converting heat power generated by jet engine into electricity

         the ratio of electric power and engine generating power
            the distributed ratio for supplementing the current power

         engine component efficiency
            the heat efficiency which each engine component has

         BLI parameters
            the relational variables with Boundary Ingestion Layer

            BLI has some options...

            various types of setting positions(ex. upper wing, upper body, down wing, upper fuselage, embedding,...)


            <Two case>
              1.simplify the effect of boundary layer as constant

              2.extend the 2D version's flow field and calculate constant in more complicated and detailed environment
                split flow into two parts(lower and higher flow)

                lower flow => velocity is equal to hub velocity of electric fan

                higher flow => velocity is equal to tip velocity of electric fan

                <average operation point method>

                fai = fai_distorted * eps / 360 + fai_freeflow * (360 - eps) / 360

                (fai = pressure ratio, thermal ratio, efficiency)


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

**Design Variables**

<Aircraft>
  fuselage shape:
     1d vector(element number = minimum 7, maximum 10)

     fuselage length(l0), section x horizontal coefficient(hx(x=1,2,3)), section x vertical coefficient(vx(x=1,2,3))

  wing shape:
     1d vector(element number = minimum 15, maximum 20)

     wing span(bx), Aspect ratio(ARx), taper ratio(tx), thickness and chord ratio(tcx), retreat angle(theta), x= main wing, vertical wing, horizontal wing

  performance:
     1d vector(element number = minimum 6, maximum 10)

     attack of angle x (x means phase, please refer to the flight path chapter)


<Engine>
  1d vector(element number = 20)

  core engine:
      OPR, TIT, Nen, technical level, engine material quality, cool air rate, x stage number, x load factor

      => x heat efficiency(x = LPC, HPC, HPT, HPTCool, LPT, LPTCool)

  turbofan engine:
      BPR, FPR, technical level => x heat efficiency(x= Fan, LPC, HPC, HPT, HPTCool, LPT, LPTCool)

  electric fan engine:
      BPRe, FPRe, Nfan, electric efficiency(conversion rate of heat into electricity), electric energy density[kg/KW]

<Joint>
  engine shape:
     1d vector(element number = 5)

     x engine mounting position(x=core engine, distributed electric fan):
        coefficient x axis, coefficient y axis(individually, based on module), turnover ratio, upper or down sign(1, -1)

  aircraft shape:
     1d vector(element number = minimum 6, maximum 12)

     x wing mounting position(x=main, vertical, horizontal):
        coefficient x axis, coefficient z axis(fuselage based)

<BLI>
     1d vector(element number = minimum 1, maximum 3)

     distortion angle(epsilon)

<Electricity>
     1d vector(element number = minimum 2, maximum 5)

     material level, battery electric energy density([kg/kw] or [kw/kg]), other args

<Mission>
     altitude, mach number, thrust at off design point, L/D, cruise range, max takeoff weight, passenger number, fuel coefficient, cargo weight ot volume





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

    subclass()
        AircraftFuselage()
            to manage the behavior against fuselage design variables

        AircraftWing()
            to manage the behavior against wing design variables(main wing, vertical wing, horizontal wing)

        AircraftPerformance()
            to manage the behavior against aircraft performance design variables

        Engine()
            to manage the behavior against engine design variables

        Joint()
            to manage the behavior against jointly part design variables

        BLI()
            to manage the required design variables for BLI(Boundary Layer Ingestion)

        Electric()
            to manage the required design variables for electric components

        Mission()
            to manage the behavior against mission's design variables


    init:
        aircraft type

        engine type

        design variables name


    method:
        concatenate_design_variables()
            to create the vector of design variables for passing the optimization module

        manage_design_variables_by_module()
            to clarify the boundary of the meaning of design variables, memorize index and name by dictionary format

        specify_fix_variables()
            to determine whether the particular design variable is fixed or not and create such design vectors


    <specification>
        deal with only engine design variables(for example, [BPR, OPR, FPR, TIT])
        deal with only aircraft design variables(for example, [wing span, aspect ratio, taper ratio, retreat angle])
        deal with only electricity(for example, [])

Mission class(define_mission.py)
    to define the mission

    mission_tuning():
        change the design variables in order to be equal to the public max takeoff weight

Aircraft parameters class(aircraft_params.py)
    to keep the aircraft parameters

    return params => numpy array  * Initialize 0 array


Aircraft performance class(aircraft_performance.py)
    to compute aerodynamic performance and weight

    aircraft aerodynamic performance class(aerodynamic_performance.py)
      calculate L/D at cruise

    aircraft weight class(aircraft_weight.py)
      class weight params()
            set_weight_params()

      calculate overall weight
      return weight results => numpy array   * Initialize 0 array

    special aircraft shape class()
      Drone class(drone.py)

      Blended Wing Body class(bwb.py)

      Hyper sonic class(hyper_sonic.py)

      Propeller class(propeller.py)


Aircraft component class(aircraft_component.py)
     base component class format()
           __init__(aircraft_params_class)
            weight = 0

            aircraft_params_class

            (needed?)

            (x, y, z) => list

            (join equipment index) => list

           run()
             feedforward()

             return None


        1: MainWing class()
           keep the main wing weight or params and calculate weight

        2: Horizontal Wing()
           keep the horizontal tail wing weight or params and calculate weight

        3: Vertical Wing()
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

        17: Furnishing()
           keep the furnishing's weight or params and calculate weight

        18: AirConditioner()
           keep the air conditioner's weight or params and calculate weight

        19: Anti Ice()
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

      Note:
          how to compute SFC and thrust is different between jet engine, propeller engine and electric engine

          <jet engine>
              SFC = mf[kg/s] / Thrust
              Thrust = m[kg/s] * (V jet - V0) + (P jet * A jet - P0 * A inlet)

          <propeller engine>
              bp = mf / Power
              power efficiency(eta p)
              Thrust = m * (V jet - V0) + (P jet * A jet - P0 * A inlet)

          <electric engine>
              if the power for driving electric fan is supplied with jet engine, the computational method is same as jet engine
              and electric power can be acquired by multiplying the electric efficiency(conversion rate of heat to electricity)

              if the power for driving electric fan is battery, the computational method is same as propeller engine
              and electric power have to be calculated in another module, which is specialized in electric performance


      design point class(engine_design_point.py)
          return thermodynamic results at design point => numpy array


      off design point class(engine_off_design_point.py)
          return thermodynamic results at off design point => numpy array

   engine weight class(engine_weight.py)
      calculate engine weight(core weight, electric fan weight, electricity weight)

      core weight class(core_engine_weight.py)
          return core weight results => numpy array  * Initialize 0 array

      electric fan weight class(electric_fan_weight.py)
          return electric fan weight results => numpy array  * Initialize 0 array

      electricity weight class(electricity_weight.py)
          special fuel engine class()
            battery class()
              calculate electric efficiency and available electric power(W or KW)

              if possible, consider the thermal management

            fuel cell class()
              calculate electric efficiency and available electric power(W or KW)

              if possible, consider the thermal management

            biological fuel class()
              calculate electric efficiency and available electric power(W or KW)

            solar battery class()
              calculate electric efficiency and available electric power(W or KW)


          return electricity weight => numpy array  * Initialize 0 array


Aircraft view class(view_aircraft.py)
     to plot the aircraft's view based on the given parameters

     class AircraftView(object):
         __init__(aircraft_component_class, engine_component_class, special_air_shape_class):
            3D aircraft coordinates array

         construct_x():
            compute 3D coordinates at each component and determine the joint position

         show():
            describe 3D plot aircraft view with engine

Engine view class(view_engine.py)
     to plot the engine's view based on given parameters

     class EngineView(object)
        __init__(engine_component_class, special_fuel_engine_class, bli_class):
           3D engine coordinates array

        construct_x():
           compute 3D coordinates at each component and determine the join position

        show():
           describe 3D plot propulsion system's view

Baseline Estimation class(estimate_baseline.py)
     to define the scale factor for aircraft design(from public value)

DataBase manage class(DataBase/database_driven.py)
     to manage the database values

Cost Estimation class(cost_estimate.py)
     to estimate the flight cost and evaluate the financial effect

Engine Component class(engine_component.py)

     **Implementation concept**

     class EngineComponent():
        __init__(name):
           name

           component index number

           next component index number

        calc_design_point_performance(design_point_result_arr, efficient_arr, settings_arr, *args):
           calculate physical values(Pressure, temperature, Area) at design point

           return design_point_result_arr

        calc_off_design_point_performance(off_design_point_result_arr, off_efficient_arr, off_settings_arr, *args):
           calculate physical values(Pressure, temperature, Area) at off design point

           return off_design_point_result_arr

        calc_diameter(engine_diameter_result_arr, design_point_result_arr, engine_settings_arr, *args):
           calculate diameter from area at design point

           return engine_diameter_result_arr or None

        calc_weight(engine_weight_result_arr, engine_settings_arr, *args):
           calculate engine weight fron engine diameter

           return engine_weight_result_arr

        --component class index number--
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


**Engine Performance**

  <off design point>
     *****Low Pressure Part*****

     0.assume the turnover rate of low pressure compressor compared to that at design point

     1.from inlet to lpc, calculate the physics values of all components

     *****High Pressure Part*****

       2.assume the turnover rate of high pressure compressor compared to that at design point

       3.from hpc to hptcool, calculate their physics values and adjust the turnover rate in order to balance the power of high pressure axis

     ---**End High Pressure Part**---

     4.from lptcool to nozzle, calculate physics values and adjust the turnover rate in order for nozzle area to be equal to that at design point

     ---**End Low Pressure Part**---

     5.finish the engine performance part at off design point and record the turnover rates of high and low pressure compressor



**Aircraft Performance**

Objective: L/D

  1.static method
    polar curve fitting

  2.accumulative method
    compute the lift and the each drag value individually and finally summarize them

    <Lift>
      L = 0.5 * rou(density) * V(Velocity of aircraft) ** 2 * S(wing area) * CL(lift coefficient)

      * constant

        AR: aspect ratio(given from input parameters)

        beta: sqrt(1 - mach number ** 2)

        eta: 0.95

        F: cross sectional coefficient, 1.07 * (1.0 + (fuselage diameter / wing width)) ** 2

        S_exposed:wing area which is exposed to outer space

        S_ref: wing area

      * subsonic case(Mach number <= 0.9)

        CL = (2 * pi * AR) / (2.0 + sqrt(4.0 + AR ** 2 * beta ** 2 / eta ** 2 * (1.0 + tan(theta * pi / 180)) ** 2 / beta ** 2) * (S_exposed / S_ref) * F

      * mixture of subsonic and hyper sonic case(0.9 <= Mach number <= 1.2)

        CL follows the drag curve and In this module, consider it as quadratic function

        ---Detail---

        slope_of_lift_left = 9.158680497060704

        slope_of_lift_right = 6.030226891555273

        a_coef = -(slope_of_lift_right - slope_of_lift_left) / (0.2 ** 2 - 0.1 ** 2)

        b_coef = slope_of_lift_left + 0.1 ** 2 * a_coef

        slope_of_lift = -a_coef * (current_mach - 1) ** 2 + b_coef

      * hyper sonic case(Mach number >= 1.2)

        CL = 4.0 / beta(constant)

    <Drag>
      types:
         D = 0.5 * rou(density) * V(Velocity) ** 2 * S(wing area) * CD(drag coefficient)

         CD = CD0 + CDi

         CD0 = sum(Cf(i) * Swet(i) / Sref)

         <induction drag(CDi)>
           CDi = CL ** 2 / (pi * e * AR)

           *e is dependent on retreat angle

           e = 1.78 * (1 - 0.045 * AR ** 0.68) - 0.64(retreat angle < 30)

           e = 4.61 * (1.0 - 0.045 * AR ** 0.68) * (np.cos(self.init_airshape_class.theta)) ** 0.15 - 3.1(retreat angle >= 30)


         <wing drag(CD0)>
           1.shape drag
             necessary parameters: Reynold number, surface roughness, representative length, mach number

             return Cf(shape drag)

           2.misc drag
             necessary parameters: angle of after fuselage, diameter of after fuselage

             return Cf(misc drag)

           3.L&P drag
             necessary parameters: the rate which L&P drag occupies in wing drag

             return Cf(L&P drag)

           4.wave drag(hyper sonic case)
             necessary parameters: fuselage diameter, fuselage length, retreat angle of main wing, mach number

             return Cf(wave drag)




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




