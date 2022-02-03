import gmsh
from math import *
import sys

gmsh.initialize()
gmsh.option.setNumber("Mesh.SaveAll", 1)
gmsh.option.setNumber("Mesh.Algorithm", 6)
gmsh.model.add("t1")
lc = 0.1
circle1 = []
N = 20

for i in range(N):
     circle1.append(gmsh.model.geo.addPoint(sin(i*2*pi/N), cos(i*2*pi/N), 0, lc))


circle2 = []


for i in range(N):
     circle2.append(gmsh.model.geo.addPoint(sin(i*2*pi/N), cos(i*2*pi/N), 1, lc))

Circle1 = []

for i in range(N):
     Circle1.append(gmsh.model.geo.addLine(circle1[i], circle1[(i+1)%N]))
Circle2 = []

for i in range(N):
     Circle2.append(gmsh.model.geo.addLine(circle2[i], circle2[(i+1)%N]))

Side = []
for i in range(N):
     Side.append(gmsh.model.geo.addLine(circle1[i], circle2[i]))

BOT = gmsh.model.geo.addCurveLoop(circle1)
TOP = gmsh.model.geo.addCurveLoop(circle2)

SIDE = []

for i in range(N):
     SIDE.append(gmsh.model.geo.addCurveLoop([Circle1[i], Side[(i+1)%N], -Circle2[i], -Side[i]]))

gmsh.model.geo.addPlaneSurface([TOP], 1)
gmsh.model.geo.addPlaneSurface([BOT], 2)
for i in range(N):
     gmsh.model.geo.addPlaneSurface([SIDE[i]], i+3)
l = gmsh.model.geo.addSurfaceLoop([i + 1 for i in range(N+2)])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()
gmsh.finalize()
