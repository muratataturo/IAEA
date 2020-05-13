import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


huf = 2.0
wf = 1.8
hlf = 2.1
upper_r = huf / wf
lower_r = hlf / wf

hau = 1.0

l1 = 8
l2 = 32
l3 = 36
l = l3

x = np.linspace(0.0, l1, 30)

def f(x):

    return np.sqrt(x)

# x => z => y
cockpit_arr = []
zupper = []
zlower = []

lower_sign = -1

for xi in x:
    z_u = huf * np.sqrt(xi / l1)
    z_l = lower_sign * hlf * np.sqrt(xi / l1)

    b_u = z_u
    a_u = b_u / upper_r

    a_l = a_u
    b_l = z_l

    y = np.linspace(-a_u, a_u, 30)

    for yi in y:
        zui = b_u * np.sqrt(1.0 - (yi / a_u) ** 2)
        zli = b_l * np.sqrt(1.0 - (yi / a_l) ** 2)
        cockpit_arr.append([xi, yi, zui])
        cockpit_arr.append([xi, yi, zli])


cabin_arr = []
x = np.linspace(l1, l2, 30)

for xi in x:
    z_u = huf
    z_l = hlf

    b_u = z_u
    a_u = b_u / upper_r

    a_l = a_u
    b_l = z_l

    y = np.linspace(-a_u, a_u, 30)

    for yi in y:
        zui = b_u * np.sqrt(1.0 - (yi / a_u) ** 2)
        zli = b_l * np.sqrt(1.0 - (yi / a_l) ** 2)

        cabin_arr.append([xi, yi, zui])
        cabin_arr.append([xi, yi, -zli])

after_cabin_arr = []
x = np.linspace(l2, l3, 30)

# upper coefficient
a1 = (huf - hau) / (np.sqrt(l2) - np.sqrt(l3))
b1 = huf - np.sqrt(l2) * a1

# lower coefficient
a2 = (hau + hlf) / (np.sqrt(l3) - np.sqrt(l2))
b2 = hau - a2 * np.sqrt(l3)

for xi in x:

    z_u = a1 * np.sqrt(xi) + b1
    z_l = a2 * np.sqrt(xi) + b2
    z_l = lower_sign * z_l

    b_u = z_u
    a_u = b_u / upper_r

    a_l = a_u
    b_l = z_l

    y = np.linspace(-a_u, a_u, 30)

    for yi in y:
        if a_u == 0:
            zui, zli = 0, 0
        else:
            zui = b_u * np.sqrt(1.0 - (yi / a_u) ** 2)
            zli = b_l * np.sqrt(1.0 - (yi / a_l) ** 2)

        if zui == 0 or zli == 0:
            continue

        after_cabin_arr.append([xi, yi, zui])
        after_cabin_arr.append([xi, yi, -zli])


# main wing
ctip = 1
croot = 5
b = 40
theta = 25

BX = croot * (b / 2 - wf) / (croot - ctip)

st = [l * 0.4, wf]

y = np.linspace(wf, b / 2, 30)

# airfoil
p = 0.4
tc = 0.11

main_wing_arr = []

for yi in y:
    xu = np.tan(theta * np.pi / 180) * (yi - wf) + st[0]
    cx = (1.0 - (yi - wf) / BX) * croot
    xl = xu + cx

    x = np.linspace(xu, xl, 30)

    for xi in x:
        zui = -tc / (p * (1 - p) * cx) * (xi - xu) * (xi - xl)
        zli = -1 * zui

        main_wing_arr.append([xi, yi, zui])
        main_wing_arr.append([xi, yi, zli])
        main_wing_arr.append([xi, -yi, zui])
        main_wing_arr.append([xi, -yi, zli])


# horizontal wing
chtip = 0.6
chroot = 1.2
bh = 15
theta = 20

BXh = chroot * (bh / 2 - wf) / (chroot - chtip)

sth = [l * 0.9, wf]

y = np.linspace(wf, bh / 2, 30)

# airfoil
p = 0.4
tc = 0.1

hori_wing_arr = []

for yi in y:
    xu = np.tan(theta * np.pi / 180) * (yi - wf) + sth[0]
    cx = (1.0 - (yi - wf) / BXh) * chroot
    xl = xu + cx

    x = np.linspace(xu, xl, 30)

    for xi in x:
        zui = -tc / (p * (1 - p) * cx) * (xi - xu) * (xi - xl)
        zli = -1 * zui

        hori_wing_arr.append([xi, yi, zui])
        hori_wing_arr.append([xi, yi, zli])
        hori_wing_arr.append([xi, -yi, zui])
        hori_wing_arr.append([xi, -yi, zli])

# vertical wing
cvtip = 0.6
cvroot = 1.2
bv = 10
theta = 45

BXv = cvroot * (bv / 2 - wf) / (cvroot - cvtip)

stv = [l * 0.95, wf]

z = np.linspace(hau, bv / 2, 30)

# airfoil
p = 0.4
tc = 0.1

vert_wing_arr = []

for zi in z:
    xu = np.tan(theta * np.pi / 180) * (zi - hau) + stv[0]
    cx = (1.0 - (zi - hau) / BXv) * cvroot
    xl = xu + cx

    x = np.linspace(xu, xl, 30)

    for xi in x:
        yui = -tc / (p * (1 - p) * cx) * (xi - xu) * (xi - xl)
        yli = -1 * yui

        vert_wing_arr.append([xi, yui, zi])
        vert_wing_arr.append([xi, yli, zi])

cockpit_arr = np.array(cockpit_arr)
cabin_arr = np.array(cabin_arr)
after_cabin_arr = np.array(after_cabin_arr)
main_wing_arr = np.array(main_wing_arr)
hori_wing_arr = np.array(hori_wing_arr)
vert_wing_arr = np.array(vert_wing_arr)

# engine(main wing down)
rin = 0.8
rout = 0.4
tin = 0.1

len = 4.0

tx = 0.2
ty = 0.2

k = 0.4

joint_point = [l * 0.4 + croot * tx, wf + (b / 2 - wf) * ty, np.min(main_wing_arr[:, 2])]

zcen = joint_point[2] - tin - rin


# engine curve -> z = ax ** 2 + b * x + c
x = np.linspace(joint_point[0] - k * len, joint_point[0] + (1 - k) * len, 30)

az = (rout - rin) / (1 - 2 * k) / len ** 2
bz = -2 * joint_point[0] * az
cz = joint_point[2] + bz ** 2 / (4 * az)

engine_arr = []

for xi in x:

    zu = az * xi ** 2 + bz * xi + cz

    zl = 2 * zcen - zu

    z = np.linspace(zl, zu, 30)

    for zi in z:
        target = np.sqrt((zu - zcen) ** 2 - (zi - zcen) ** 2)
        yui = joint_point[1] + target
        yli = joint_point[1] - target

        engine_arr.append([xi, yui, zi])
        engine_arr.append([xi, yli, zi])
        engine_arr.append([xi, -yui, zi])
        engine_arr.append([xi, -yli, zi])


engine_arr = np.array(engine_arr)

# engine(main wing upper)
upper_sign = 1
joint_point = [l * 0.4 + croot * tx, wf + (b / 2 - wf) * ty, np.max(main_wing_arr[:, 2])]

zcen = joint_point[2] + tin + rin

# engine curve -> z = ax ** 2 + b * x + c
x = np.linspace(joint_point[0] - k * len, joint_point[0] + (1 - k) * len, 30)

az = (rin - rout) / (1 - 2 * k) / len ** 2
bz = -2 * joint_point[0] * az
cz = joint_point[2] + bz ** 2 / (4 * az)

engine_arr_up = []

for xi in x:

    zl = az * xi ** 2 + bz * xi + cz

    zu = 2 * zcen - zl

    z = np.linspace(zl, zu, 30)

    for zi in z:
        target = np.sqrt((zu - zcen) ** 2 - (zi - zcen) ** 2)
        yui = joint_point[1] + target
        yli = joint_point[1] - target

        engine_arr_up.append([xi, yui, zi])
        engine_arr_up.append([xi, yli, zi])
        engine_arr_up.append([xi, -yui, zi])
        engine_arr_up.append([xi, -yli, zi])


engine_arr_up = np.array(engine_arr_up)



"""
# base code
# x => y => z
arr = []
for xi in x:
    y_t = f(xi)
    y = np.linspace(0.0, y_t, 50)

    a = y_t
    b = y_t * a_to_b

    for yi in y:
        if a == 0:
            zi = 0
        else:
            zi = b * np.sqrt(1.0 - yi ** 2 / a ** 2)

        arr.append([xi, yi, zi])
        arr.append([xi, yi, -zi])
        arr.append([xi, -yi, zi])
        arr.append([xi, -yi, -zi])

"""

fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(cockpit_arr[:, 0], cockpit_arr[:, 1], cockpit_arr[:, 2])
ax.scatter(cabin_arr[:, 0], cabin_arr[:, 1], cabin_arr[:, 2])
ax.scatter(after_cabin_arr[:, 0], after_cabin_arr[:, 1], after_cabin_arr[:, 2])
ax.scatter(main_wing_arr[:, 0], main_wing_arr[:, 1], main_wing_arr[:, 2])
ax.scatter(hori_wing_arr[:, 0], hori_wing_arr[:, 1], hori_wing_arr[:, 2])
ax.scatter(vert_wing_arr[:, 0], vert_wing_arr[:, 1], vert_wing_arr[:, 2])
# ax.scatter(engine_arr[:, 0], engine_arr[:, 1], engine_arr[:, 2])
ax.scatter(engine_arr_up[:, 0], engine_arr_up[:, 1], engine_arr_up[:, 2])

ax.set_xlim([-10, 40])
ax.set_ylim([-20, 20])
ax.set_zlim([-10, 10])

plt.show()




