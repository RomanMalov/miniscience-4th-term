# ------------------------------------------------------------------------------
#
#  Gmsh Python tutorial 1
#
#  Geometry basics, elementary entities, physical groups
#
# ------------------------------------------------------------------------------

# The Python API is entirely defined in the `gmsh.py' module (which contains the
# full documentation of all the functions in the API):
import gmsh
import sys
from math import pi

# Before using any functions in the Python API, Gmsh must be initialized:
gmsh.initialize()

# Next we add a new model named "t1" (if gmsh.model.add() is not called a new
# unnamed model will be created on the fly, if necessary):
gmsh.model.add("t1")

# The Python API provides direct access to each supported geometry (CAD)
# kernel. The built-in kernel is used in this first tutorial: the corresponding
# API functions have the `gmsh.model.geo' prefix.

# The first type of `elementary entity' in Gmsh is a `Point'. To create a point
# with the built-in CAD kernel, the Python API function is
# gmsh.model.geo.addPoint():
# - the first 3 arguments are the point coordinates (x, y, z)
# - the next (optional) argument is the target mesh size close to the point
# - the last (optional) argument is the point tag (a stricly positive integer
#   that uniquely identifies the point)
lc = 1e-2


# The distribution of the mesh element sizes will be obtained by interpolation
# of these mesh sizes throughout the geometry. Another method to specify mesh
# sizes is to use general mesh size Fields (see `t10.py'). A particular case is
# the use of a background mesh (see `t7.py').
#
# If no target mesh size of provided, a default uniform coarse size will be used
# for the model, based on the overall model size.
#
# We can then define some additional points. All points should have different
# tags:


# If the tag is not provided explicitly, a new tag is automatically created, and
# returned by the function:

# Curves are Gmsh's second type of elementery entities, and, amongst curves,
# straight lines are the simplest. The API to create straight line segments with
# the built-in kernel follows the same conventions: the first 2 arguments are
# point tags (the start and end points of the line), and the last (optional one)
# is the line tag.
#
# In the commands below, for example, the line 1 starts at point 1 and ends at
# point 2.
#
# Note that curve tags are separate from point tags - hence we can reuse tag `1'
# for our first curve. And as a general rule, elementary entity tags in Gmsh
# have to be unique per geometrical dimension.


# The third elementary entity is the surface. In order to define a simple
# rectangular surface from the four curves defined above, a curve loop has first
# to be defined. A curve loop is defined by an ordered list of connected curves,
# a sign being associated with each curve (depending on the orientation of the
# curve to form a loop). The API function to create curve loops takes a list
# of integers as first argument, and the curve loop tag (which must be unique
# amongst curve loops) as the second (optional) argument:
gmsh.model.occ.addCircle(0.0, 0.0, 0.0,100.0,1,angle1=0.,angle2=2*pi)
# We can then define the surface as a list of curve loops (only one here,
# representing the external contour, since there are no holes--see `t4.py' for
# an example of a surface with a hole):
gmsh.model.geo.addPlaneSurface([1], 1)

# Before they can be meshed (and, more generally, before they can be used by API
# functions outside of the built-in CAD kernel functions), the CAD entities must
# be synchronized with the Gmsh model, which will create the relevant Gmsh data
# structures. This is achieved by the gmsh.model.geo.synchronize() API call for
# the built-in CAD kernel. Synchronizations can be called at any time, but they
# involve a non trivial amount of processing; so while you could synchronize the
# internal CAD data after every CAD command, it is usually better to minimize
# the number of synchronization points.
gmsh.model.geo.synchronize()

# At this level, Gmsh knows everything to display the rectangular surface 1 and
# to mesh it. An optional step is needed if we want to group elementary
# geometrical entities into more meaningful groups, e.g. to define some
# mathematical ("domain", "boundary"), functional ("left wing", "fuselage") or
# material ("steel", "carbon") properties.
#
# Such groups are called "Physical Groups" in Gmsh. By default, if physical
# groups are defined, Gmsh will export in output files only mesh elements that
# belong to at least one physical group. (To force Gmsh to save all elements,
# whether they belong to physical groups or not, set the `Mesh.SaveAll' option
# to 1.) Physical groups are also identified by tags, i.e. stricly positive
# integers, that should be unique per dimension (0D, 1D, 2D or 3D). Physical
# groups can also be given names.
#
# Here we define a physical curve that groups the left, bottom and right curves
# in a single group (with prescribed tag 5); and a physical surface with name
# "My surface" (with an automatic tag) containing the geometrical surface 1:
#gmsh.model.addPhysicalGroup(1, [1, 2, 4], 5)
#ps = gmsh.model.addPhysicalGroup(2, [1])
#gmsh.model.setPhysicalName(2, ps, "My surface")

# We can then generate a 2D mesh...
gmsh.model.mesh.generate(2)

# ... and save it to disk
gmsh.write("t1.msh")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()


gmsh.finalize()

