import gmsh
import sys

gmsh.initialize()

gmsh.model.add("t2")

lc = 1e-1
'''gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(.1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(0, .1, 0, lc, 3)
gmsh.model.geo.addPoint(0, 0, 0.2, lc, 4)

gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 3, 2)
gmsh.model.geo.addLine(3, 1, 3)

for i in range(3):
    gmsh.model.geo.addLine(i + 1, 4, i + 4)'''

for i in range(2):
    for j in range(2):
        for k in range(2):
            gmsh.model.geo.addPoint(i, j, k, lc, 4*i+2*j+k)

for i1 in range(2):
    for j1 in range(2):
        for k1 in range(2):
            for i2 in range(2):
                for j2 in range(2):
                    for k2 in range(2):
                        if (i1-i2)**2+(j1-j2)**2+(k1-k2)**2==1 and 4*i1+2*j1+k1>4*i2+2*j2+k2:
                            gmsh.model.geo.addLine(4*i1+2*j1+k1, 4*i2+2*j2+k2, 10*(4*i1+2*j1+k1)+4*i2+2*j2+k2)




gmsh.model.geo.addCurveLoop([20, 62, -64, -40], 1)
gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.addCurveLoop([20, 32, -31, -10], 2)
gmsh.model.geo.addPlaneSurface([2], 2)

gmsh.model.geo.addCurveLoop([10, 51, -54, -40], 3)
gmsh.model.geo.addPlaneSurface([3], 3)

gmsh.model.geo.addCurveLoop([31, 73, -75, -51], 4)
gmsh.model.geo.addPlaneSurface([4], 4)

gmsh.model.geo.addCurveLoop([32, 73, -76, -62], 5)
gmsh.model.geo.addPlaneSurface([5], 5)

gmsh.model.geo.addCurveLoop([64, 76, -75, -54], 6)
gmsh.model.geo.addPlaneSurface([6], 6)

'''gmsh.model.geo.addCurveLoop([1, 2, 3], 1)
gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.addCurveLoop([1, 5, -4], 2)
gmsh.model.geo.addPlaneSurface([2], 2)

gmsh.model.geo.addCurveLoop([2, 6, -5], 3)
gmsh.model.geo.addPlaneSurface([3], 3)

gmsh.model.geo.addCurveLoop([3, 4, -6], 4)
gmsh.model.geo.addPlaneSurface([4], 4)'''

l = gmsh.model.geo.addSurfaceLoop([i + 1 for i in range(6)])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)

gmsh.write("t2.msh")
gmsh.write("t2.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()

