import math


class Physics(object):
    """
    --Attributes--
        r0: constant value of geo potential [km], type(double)

        H : reference value of geo potential [km], type(double)

        ****reference value(0 m)****

        T0: reference value of static temperature [K], type(double)

        P0: reference value of static pressure [pa], type(double)

        ref_K: absolute zero [K], type(double)

        T: static temperature [K], type(double)

        P: static pressure [pa], type(double)

        rou: density [kg/m^3], type(double)

        rou0: reference value of density [kg/m^3]

        a: tone velocity [m/s]

        a0: reference value of tone velocity [m/s]

        mu: viscosity [Ns/m^2]

        mu0: reference value of viscosity [Ns/m^2]

        kai: dynamic viscosity [m^2/s]

        kai0: reference value of dynamic viscosity

    --Method--
        geo_potential(): calculate geo potential

        temperature_and_pressure(): compute static temperature and pressure

        density(): calculate density, P = n * R * T

        velocity(): calculate tone velocity, a = sqrt(gamma * R * T)

        viscosity(): calculate viscosity

        dynamic_viscosity(): calculate dynamic viscosity



    """

    def __init__(self, altitude):
        """

        :param altitude: type double, cruise altitude
        """

        # constant for geo potential
        self.r0 = 6356.766  # [km]
        # geo potential
        self.H = altitude

        if self.H >= 1000:

            self.H /= 1000

        self.geo_potential()

        # temperature and pressure
        self.T0 = 15  # [K]
        self.P0 = 101325  # [pa]
        self.ref_K = 273.15  # absolute zero

        # Initialize static Temperature and Pressure at current altitude
        self.T = 0
        self.P = 0

        # compute static temperature and pressure
        self.temperature_and_pressure()

        # density
        self.rou = 0
        self.rou0 = 1.225  # [kg/m^3] value at 0[m]
        self.density()

        # velocity
        self.a = 0
        self.a0 = 340.29  # [m/s]  value at 0[m]
        self.velocity()

        # viscosity
        self.mu = 0
        self.mu0 = 1.7849 * 1e-5  # [Ns/m^2]  value at 0[m]
        self.viscosity()

        # dynamic viscosity
        self.kai = 0
        self.kai0 = 1.4607 * 1e-5  # [m^2/s]  value at 0[m]
        self.dynamic_viscosity()

    def geo_potential(self):
        """
        calculate geo potential
        :return: None
        """

        self.H = self.r0 * self.H / (self.r0 + self.H)

    def temperature_and_pressure(self):
        """
        calculate static temperature and pressure
        :return:
        """

        if 0 <= self.H <= 11:
            self.T = self.T0 - 6.5 * self.H
            self.P = self.P0 * (288.15 / (self.T + self.ref_K)) ** (-5.256)

        elif 11 <= self.H <= 20.0:
            self.T = -56.5
            self.P = 22632.064 * math.exp(-0.1577 * (self.H - 11))

        elif 20.0 <= self.H <= 32.0:
            self.T = -76.5 + self.H
            self.P = 5474.889 * (216.65 / (self.T + self.ref_K)) ** 34.163

        elif 32.0 <= self.H <= 47.0:
            self.T = -134.1 + 2.8 * self.H
            self.P = 868.019 * (228.65 / (self.T + self.ref_K)) ** 12.201

        elif 47.0 <= self.H <= 51:
            self.T = -2.5
            self.P = 110.906 * math.exp(-0.1262 * (self.H - 47))

        elif 51 <= self.H <= 71:
            self.T = 140.3 - 2.8 * self.H
            self.P = 66.939 * (270.65 / (self.T + self.ref_K)) ** (-12.201)

        elif 71 <= self.H <= 84.852:
            self.T = 83.5 - 2.0 * self.H
            self.P = 3.956 * (214.56 / (self.T + self.ref_K)) ** (-17.082)

        # change [K] units
        self.T += self.ref_K

    def density(self):
        """
        calculate density at cruise altitude
        :return: None
        """

        self.rou = 0.0034837 * self.P / self.T

    def velocity(self):
        """
        calculate tone velocity
        :return: None
        """

        self.a = 20.0468 * math.sqrt(self.T)

    def viscosity(self):
        """
        calculate viscosity
        S : Sutherland constant
        beta: constant
        :return: None
        """

        S = 110.4  # サザーランド定数
        beta = 1.458e-6  # 係数
        self.mu = beta * self.T ** 1.5 / (self.T + S)

    def dynamic_viscosity(self):
        """
        calculate dynamic viscosity
        :return: None
        """

        self.kai = self.mu / self.rou










