import gmsh
from math import *
import sys

gmsh.initialize()
gmsh.option.setNumber("Mesh.SaveAll", 1)
gmsh.option.setNumber("Mesh.Algorithm", 6)
gmsh.model.add("t1")
lc = 0.5
circle1 = []
A = 20

B = 20


def surftorus(R1, R2):
    dots = []
    for i in range(A):
        dots1 = []
        for j in range(B):
            dots1.append(gmsh.model.geo.addPoint(R1 * sin(i * 2 * pi / A) * (1 + R2 / R1 * cos(j * 2 * pi / B)),
                                                 R1 * cos(i * 2 * pi / A) * (1 + R2 / R1 * cos(j * 2 * pi / B)),
                                                 R2 * sin(j * 2 * pi / B), lc))
        dots.append(dots1)
    lines_hor = []
    for i in range(A):
        lines_hor1 = []
        for j in range(B):
            lines_hor1.append(gmsh.model.geo.addLine(dots[i][j], dots[(i + 1) % A][j]))
        lines_hor.append(lines_hor1)
    lines_ver = []
    for i in range(A):
        lines_ver1 = []
        for j in range(B):
            lines_ver1.append(gmsh.model.geo.addLine(dots[i][j], dots[i][(j + 1) % B]))
        lines_ver.append(lines_ver1)
    surf = []
    for i in range(A):
        surf1 = []
        for j in range(B):
            surf1.append(gmsh.model.geo.addCurveLoop([ lines_ver[i][j], lines_hor[i][(j+1)%B], -lines_ver[(i+1)%A][j], -lines_hor[i][j]]))
        surf.append(surf1)
    SURF = []
    for i in range(A):
        for j in range(B):
            SURF.append(gmsh.model.geo.addPlaneSurface([surf[i][j]]))
    return gmsh.model.geo.addSurfaceLoop(SURF)


gmsh.model.geo.addVolume([surftorus(5, 2), -surftorus(5, 1)])

gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()
gmsh.finalize()
