import gmsh
from math import *
import sys

gmsh.initialize()
gmsh.option.setNumber("Mesh.SaveAll", 1)
gmsh.option.setNumber("Mesh.Algorithm", 6)
gmsh.model.add("t1")
lc = 0.1
A1 = gmsh.model.geo.addPoint(1, 0, 0, lc)
B1 = gmsh.model.geo.addPoint(0, 1, 0, lc)
C1 = gmsh.model.geo.addPoint(-1, 0, 0, lc)
D1 = gmsh.model.geo.addPoint(0, -1, 0, lc)
O1 = gmsh.model.geo.addPoint(0, 0, 0, lc)

A2 = gmsh.model.geo.addPoint(1, 0,  1, lc)
B2 = gmsh.model.geo.addPoint(0, 1,  1, lc)
C2 = gmsh.model.geo.addPoint(-1, 0, 1, lc)
D2 = gmsh.model.geo.addPoint(0, -1,  1, lc)
O2 = gmsh.model.geo.addPoint(0, 0,  1, lc)

arc1 = gmsh.model.geo.addCircleArc(A1, O1, B1)
arc2 = gmsh.model.geo.addCircleArc(B1, O1, C1)
arc3 = gmsh.model.geo.addCircleArc(C1, O1, D1)
arc4 = gmsh.model.geo.addCircleArc(D1, O1, A1)

Arc1 = gmsh.model.geo.addCircleArc(A2, O2, B2)
Arc2 = gmsh.model.geo.addCircleArc(B2, O2, C2)
Arc3 = gmsh.model.geo.addCircleArc(C2, O2, D2)
Arc4 = gmsh.model.geo.addCircleArc(D2, O2, A2)



l1 = gmsh.model.geo.addLine(A1, A2)
l2 = gmsh.model.geo.addLine(B1, B2)
l3 = gmsh.model.geo.addLine(C1, C2)
l4 = gmsh.model.geo.addLine(D1, D2)


BOT = gmsh.model.geo.addCurveLoop([arc1, arc2, arc3, arc4])
TOP = gmsh.model.geo.addCurveLoop([Arc1, Arc2, Arc3, Arc4])
s1 = gmsh.model.geo.addCurveLoop([ -l1, arc1,  l2, -Arc1])
s2 = gmsh.model.geo.addCurveLoop([ -l2, arc2,  l3, -Arc2])

s3 = gmsh.model.geo.addCurveLoop([ -l3, arc3,  l4, -Arc3])
s4 = gmsh.model.geo.addCurveLoop([ -l4, arc4,  l1, -Arc4])


gmsh.model.geo.addPlaneSurface([s1], 1)
gmsh.model.geo.addPlaneSurface([s2], 2)
gmsh.model.geo.addPlaneSurface([s3], 3)
gmsh.model.geo.addPlaneSurface([s4], 4)

gmsh.model.geo.addPlaneSurface([BOT], 5)

gmsh.model.geo.addPlaneSurface([TOP], 6)

l = gmsh.model.geo.addSurfaceLoop([i + 1 for i in range(6)])
gmsh.model.geo.addVolume([l])


gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()
gmsh.finalize()
