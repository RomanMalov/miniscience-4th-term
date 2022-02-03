import gmsh
from math import *
import sys

gmsh.initialize()
gmsh.option.setNumber("Mesh.SaveAll", 1)
gmsh.option.setNumber("Mesh.Algorithm", 6)
gmsh.model.add("t1")
lc = 10e-3
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(0.5, 0, 0, lc, 2)
gmsh.model.geo.addPoint(1, 0, 0, lc, 3)

gmsh.model.geo.addCircleArc(1, 2,  3, 1)
gmsh.model.geo.addCircleArc(3, 2,  1, 2)


gmsh.model.geo.addCurveLoop([1, 2] ,2)


gmsh.model.geo.addPlaneSurface([2],1)
l = gmsh.model.geo.addSurfaceLoop([])
gmsh.model.geo.addVolume([l])
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(2)
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()
gmsh.finalize()