import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

huf = 1.5
hlf = 0.2
wf = 1.2

hau = 0.3

upper_r = huf / wf
upper_l = hlf / wf

l1 = 3
l2 = 6
l3 = 7

l = l3

# cockpit part
x = np.linspace(0, l1, 30)

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

cockpit_arr = np.array(cockpit_arr)

# cabin part
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

cabin_arr = np.array(cabin_arr)


# after cabin part
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

after_cabin_arr = np.array(after_cabin_arr)

# propeller(4)
def turnover_3d(theta, n):
    t_arr = np.array([[np.cos(theta) + n[0] ** 2 * (1 - np.cos(theta)),
                       n[0] * n[1] * (1 - np.cos(theta)) - n[2] * np.sin(theta),
                       n[2] * n[1] * (1 - np.cos(theta)) + n[1] * np.sin(theta)],
                      [n[0] * n[1] * (1 - np.cos(theta)) + n[2] * np.sin(theta),
                       np.cos(theta) + n[1] ** 2 * (1 - np.cos(theta)),
                       n[1] * n[2] * (1 - np.cos(theta)) - n[0] * np.sin(theta)],
                      [n[2] * n[0] * (1 - np.cos(theta)) - n[1] * np.sin(theta),
                       n[1] * n[2] * (1 - np.cos(theta)) + n[0] * np.sin(theta),
                       np.cos(theta) + n[2] ** 2 * (1 - np.cos(theta))]])

    return t_arr

# propeller settings
txs = [0.5, 0.65, 0.75, 0.9]
thetas = [50, 20, -20, -50]

radius = 1.0
pr = 0.5
lp = 0.5

k = 0.3

half_propeller_number = len(txs)

joint_points = []

for idx in range(half_propeller_number):
    point = [l * txs[idx], np.max(cabin_arr[:, 1]), 0]
    joint_points.append(point)

propeller_arr_l = []
propeller_arr_r = []

unit_vec = np.array([1, 0, 0])

for theta, joint_point in zip(thetas, joint_points):
    center = np.array([joint_point[0] - (radius + pr) * np.sin(theta * np.pi / 180.0), joint_point[1] + (radius + pr) * np.cos(theta * np.pi / 180.0), joint_point[2]])

    z = np.linspace(-k * lp, (1 - k) * lp, 30)

    for zi in z:

        x = np.linspace(center[0] - pr, center[0] + pr, 30)

        for xi in x:
            target = np.sqrt(pr ** 2 - (xi - center[0]) ** 2)
            yui = center[1] + target
            yli = center[1] - target

            plu = [xi, yui, zi]
            pll = [xi, yli, zi]
            propeller_arr_l.append(plu)
            propeller_arr_l.append(pll)

            pru = [xi, -yui, zi]
            prl = [xi, -yli, zi]
            propeller_arr_r.append(pru)
            propeller_arr_r.append(prl)


propeller_arr_l = np.array(propeller_arr_l)
propeller_arr_r = np.array(propeller_arr_r)

# z axis 3d turnover
propeller_arr = np.concatenate([propeller_arr_l, propeller_arr_r], axis=0)

# poll
poll_r = 0.1

poll_arr = []

for idx in range(half_propeller_number):

    rep_j = joint_points[idx]
    x = np.linspace(0, radius + pr, 30)

    t_arr = turnover_3d(thetas[idx] - 90, np.array([0, 0, 1]))

    for xi in x:
        y = np.linspace(- poll_r, poll_r, 30)

        for yi in y:
            target = np.sqrt(poll_r ** 2 - yi ** 2)
            zui = target
            zli = - target

            pu = [xi, yi, zui]
            pl = [xi, yi, zli]
            poll_arr.append(pu)
            poll_arr.append(pl)

            puu = np.dot(t_arr.T, np.array(pu)) + np.array([rep_j[0], rep_j[1], rep_j[2]])
            pll = np.dot(t_arr.T, np.array(pl)) + np.array([rep_j[0], rep_j[1], rep_j[2]])
            poll_arr.append(puu.tolist())
            poll_arr.append(pll.tolist())


poll_arr = np.array(poll_arr)

# 3D plot
fig = plt.figure()

ax = Axes3D(fig)

ax.scatter(cockpit_arr[:, 0], cockpit_arr[:, 1], cockpit_arr[:, 2])
ax.scatter(cabin_arr[:, 0], cabin_arr[:, 1], cabin_arr[:, 2])
ax.scatter(after_cabin_arr[:, 0], after_cabin_arr[:, 1], after_cabin_arr[:, 2])
ax.scatter(propeller_arr[:, 0], propeller_arr[:, 1], propeller_arr[:, 2])
ax.scatter(poll_arr[:, 0], poll_arr[:, 1], poll_arr[:, 2])

ax.set_xlim([-2, 8])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

plt.show()




