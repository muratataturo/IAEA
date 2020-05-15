import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# ToDo: arrange and clarify the arguments and split the module based on function
huf = 2.0  # upper fuselage height (radius)
wf = 1.8  # fuselage width (radius)
hlf = 2.1  # lower fuselage height(fuselage), optimize it from cargo volume
upper_r = huf / wf  # the ratio of height and width at upper part
lower_r = hlf / wf  # the ratio of height and width at lower part

hau = 1.0  # height of after cabin upper

l1 = 8  # up to section 1 length
l2 = 32  # up to section 2 length
l3 = 36  # up to section 3 length
l = l3  # total fuselage length

x = np.linspace(0.0, l1, 30)

# ToDo: repair the implementation by bezier curve
# cockpit
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
lower = -1
rin = 0.8
rout = 0.4
tin = 0.1

len = 4.0

tx = 0.2
ty = 0.2

k = 0.4

joint_point = [l * 0.4 + croot * tx, wf + (b / 2 - wf) * ty, lower * np.max(main_wing_arr[:, 2])]

zcen = joint_point[2] - tin - rin


# engine curve -> z = ax ** 2 + b * x + c
x = np.linspace(joint_point[0] - k * len, joint_point[0] + (1 - k) * len, 30)

az = lower * (rin - rout) / (1 - 2 * k) / len ** 2
bz = -2 * joint_point[0] * az
cz = joint_point[2] + bz ** 2 / (4 * az)

engine_arr_low = []

for xi in x:

    zu = az * xi ** 2 + bz * xi + cz

    zl = 2 * zcen - zu

    z = np.linspace(zl, zu, 30)

    for zi in z:
        target = np.sqrt((zu - zcen) ** 2 - (zi - zcen) ** 2)
        yui = joint_point[1] + target
        yli = joint_point[1] - target

        engine_arr_low.append([xi, yui, zi])
        engine_arr_low.append([xi, yli, zi])
        engine_arr_low.append([xi, -yui, zi])
        engine_arr_low.append([xi, -yli, zi])


engine_arr_low = np.array(engine_arr_low)

# engine(main wing upper)
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

# engine(upper fuselage)
rin = 0.8
rout = 0.4
tin = 0.1

k = 0.4
len = 5.0

theta = 30
tx = 0.7

eca = np.max(cabin_arr[:, 1])
ecb = np.max(cabin_arr[:, 2])

r = np.sqrt((eca * np.cos(theta * np.pi / 180.0)) ** 2 + (ecb * np.cos(theta * np.pi / 180.0) ** 2))

joint_point = [l * tx, r * np.cos(theta * np.pi / 180.0), r * np.sin(theta * np.pi / 180.0)]

zcen = (r + rin + tin) * np.sin(theta * np.pi / 180.0)

az = (rin - rout) * np.cos(theta * np.pi / 180.0) / (1 - 2 * k) / len ** 2
bz = (k * len - 2 * joint_point[0]) * az - tin * np.cos(theta * np.pi / 180.0) / (k * len)
cz = joint_point[2] - (rin + tin) * np.cos(theta * np.pi / 180.0) - az * joint_point[0] ** 2 - bz * joint_point[0]

x = np.linspace(joint_point[0] - k * len, joint_point[0] + (1 - k) * len, 30)

engine_fus_arr_up = []

for xi in x:
    zl = az * xi ** 2 + bz * xi + cz
    zu = zl + (zcen - zl) * 2

    z = np.linspace(zl, zu, 30)

    for zi in z:
        target = np.sqrt((zu - zcen) ** 2 - (zi - zcen) ** 2)
        yui = joint_point[1] + target
        yli = joint_point[1] - target

        engine_fus_arr_up.append([xi, yui, zi])
        engine_fus_arr_up.append([xi, yli, zi])
        engine_fus_arr_up.append([xi, -yui, zi])
        engine_fus_arr_up.append([xi, -yli, zi])


engine_fus_arr_up = np.array(engine_fus_arr_up)


fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(cockpit_arr[:, 0], cockpit_arr[:, 1], cockpit_arr[:, 2])
ax.scatter(cabin_arr[:, 0], cabin_arr[:, 1], cabin_arr[:, 2])
ax.scatter(after_cabin_arr[:, 0], after_cabin_arr[:, 1], after_cabin_arr[:, 2])
ax.scatter(main_wing_arr[:, 0], main_wing_arr[:, 1], main_wing_arr[:, 2])
ax.scatter(hori_wing_arr[:, 0], hori_wing_arr[:, 1], hori_wing_arr[:, 2])
ax.scatter(vert_wing_arr[:, 0], vert_wing_arr[:, 1], vert_wing_arr[:, 2])
ax.scatter(engine_arr_low[:, 0], engine_arr_low[:, 1], engine_arr_low[:, 2])
ax.scatter(engine_arr_up[:, 0], engine_arr_up[:, 1], engine_arr_up[:, 2])
ax.scatter(engine_fus_arr_up[:, 0], engine_fus_arr_up[:, 1], engine_fus_arr_up[:, 2])

ax.set_xlim([-10, 40])
ax.set_ylim([-20, 20])
ax.set_zlim([-10, 10])

# plt.savefig('./Pictures/normal.png')

plt.show()




