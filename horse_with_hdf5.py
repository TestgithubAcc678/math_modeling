import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import shapely.geometry as geom
import h5py

fig, ax = plt.subplots()


def circle(R, x0, y0, t0, t1):
    t=np.arange(t0, t1, 0.1)
    x = R * np.cos(t)+x0
    y = R * np.sin(t)+y0
    return x, y

def circle_r(R, x0, y0, t0, t1):
    t=np.arange(t1, t0, -0.1)
    x = R * np.cos(t)+x0
    y = R * np.sin(t)+y0
    return x, y

coords = circle(450, 100, 1100, -1.79, -0.5)

coords_1 = circle_r(240, 660, 695, 6.7, 8.6)  
x = np.append(coords[0], coords_1[0])
y = np.append(coords[1], coords_1[1])


coords_line = np.array([[870, 890], [805, 630]])
x = np.append(x, coords_line[0])
y = np.append(y, coords_line[1])


coords_3 = circle(50, 940, 615, 3.05, 4.05)
x = np.append(x, coords_3[0])
y = np.append(y, coords_3[1])


coords_4 = circle(150, 770, 500, 6.8, 8)
x = np.append(x, coords_4[0])
y = np.append(y, coords_4[1])


coords_5 = circle(50, 740, 600, 1.4, 4.9)
x = np.append(x, coords_5[0])
y = np.append(y, coords_5[1])


coords_6 = circle_r(100, 770, 450, 6, 8.1)
x = np.append(x, coords_6[0])
y = np.append(y, coords_6[1])


coords_7 = circle_r(250, 1040, 230, 1.5, 2.4)
x = np.append(x, coords_7[0])
y = np.append(y, coords_7[1])


coords_8 = circle(150, 1025, 625, 4.7, 6.5)
x = np.append(x, coords_8[0])
y = np.append(y, coords_8[1])

coords_line = np.array([[1175, 1140], [630, 940]])
x = np.append(x, coords_line[0])
y = np.append(y, coords_line[1])


coords_10 = circle(55, 1083, 945, 6.4, 7.9)
x = np.append(x, coords_10[0])
y = np.append(y, coords_10[1])

coords_line = np.array([[1080, 1070], [1000, 1080]])
x = np.append(x, coords_line[0])
y = np.append(y, coords_line[1])


coords_line = np.array([[1079, 1170], [1085, 1115]])
x = np.append(x, coords_line[0])
y = np.append(y, coords_line[1])


coords_line = np.array([[1171, 1210], [1116, 1280]])
x = np.append(x, coords_line[0])
y = np.append(y, coords_line[1])


coords_14 = circle_r(170, 1373, 1230, 1.2, 3)
x = np.append(x, coords_14[0])
y = np.append(y, coords_14[1])


coords_line = np.array([[1440, 1710], [1385, 1270]])
x = np.append(x, coords_line[0])
y = np.append(y, coords_line[1])


coords_16 = circle(200, 1802, 1448, -2, -0.9)
x = np.append(x, coords_16[0])
y = np.append(y, coords_16[1])

coords_line = np.array([[1915, 1915], [1283, 1435]])
x = np.append(x, coords_line[0])
y = np.append(y, coords_line[1])

coords_line = np.array([[1916, 0], [1436, 1436]])
x = np.append(x, coords_line[0])
y = np.append(y, coords_line[1])

coords_line = np.array([[10, 10], [1430, 660]])
x = np.append(x, coords_line[0])
y = np.append(y, coords_line[1])

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

coords = []
for i in range(len(spline_curve[0])):
    coords.append([spline_curve[0][i], spline_curve[1][i]])

poly = geom.Polygon(coords)
pointsnumber = 500
x_limits = [0, 1916]
y_limits = [0, 1436]

points_x, points_y = [], []
for x_coord in np.linspace(*x_limits, pointsnumber):
    for y_coord in np.linspace(*y_limits, pointsnumber):
        p = geom.Point(x_coord, y_coord)
        if p.within(poly):
            points_x.append(x_coord)
            points_y.append(y_coord)

x = np.array(points_x)
y = np.array(points_y)


float_type = np.float64
int_type = np.int32

box_size = 2000

gas_part_num = len(x)
gas_coords = np.zeros([gas_part_num, 3], dtype=float_type)
for i in range(len(x)):
    gas_coords[i][0] = x[i]
    gas_coords[i][1] = y[i]
gas_vel = np.ndarray([gas_part_num, 3], dtype=float_type)
gas_masses = np.ones(gas_part_num, dtype=float_type)


##############################################
IC = h5py.File('IC_1.hdf5', 'w')
header = IC.create_group("Header")
part0 = IC.create_group("PartType0")

KEY_STUB = 0
KEY_STUB_ARRAY = np.ones(6, dtype = int_type)
num_part = np.array([gas_part_num, 0, 0, 0, 0, 0], dtype=int_type)
header.attrs.create("NumPart_ThisFile", num_part)
header.attrs.create("NumPart_Total_HighWord", np.zeros(6, dtype=int_type))
header.attrs.create("NumPart_Total", num_part)
header.attrs.create("MassTable", KEY_STUB_ARRAY)
header.attrs.create("Time", KEY_STUB)
header.attrs.create("BoxSize", KEY_STUB)
header.attrs.create("Redshift", KEY_STUB)
header.attrs.create("Omega0", KEY_STUB)
header.attrs.create("OmegaB", KEY_STUB)
header.attrs.create("OmegaLambda", KEY_STUB)
header.attrs.create("HubbleParam", KEY_STUB)
header.attrs.create("Flag_Sfr", KEY_STUB)
header.attrs.create("Flag_Cooling", KEY_STUB)
header.attrs.create("Flag_StellarAge", KEY_STUB)
header.attrs.create("Flag_Metals", KEY_STUB)
header.attrs.create("Flag_Feedback", KEY_STUB)
header.attrs.create("NumFilesPerSnapshot", KEY_STUB)
header.attrs.create("Flag_DoublePrecision", 1)

part0.create_dataset("ParticleIDs", data=np.arange(0, gas_part_num))
part0.create_dataset("Coordinates", data=gas_coords)
part0.create_dataset("Velocities", data=gas_vel)
part0.create_dataset("Masses", data=gas_masses)

IC.close()