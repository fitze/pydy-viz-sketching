# I hope all objects have a name property; very helpful for debugging, and just in general.

class Visualization(object):
    
    def __init__(self, name):
        pass
    
    @property
    def scene(self):
        pass

class Scene(object):

    def __init__(self, name):
        pass
    
    @property
    def visualization_frames(self):
        pass

    def visualization_frame_new(self, vframe):
        self._visualization_frames.append(vframe)

    def draw():
        for frame in self._visualization_frames:
            frame.draw()
    

class VisualizationFrame(object):
    
    def __init__(self, name, origin, rotation_matrix):
        pass
    
    @property
    def shapes(self):
        # Other packages call this Geom or Geometry. I know we agree circles, 
        # spheres, cylinders are shapes, but is a mesh a shape too?
        # Shape needs to be a class that can draw itself (see below)
        pass
    
    @property
    def origin(self):
        pass
    
    @property
    def rotation_matrix(self):
        pass
    
    # ALTERNATIVELY:
    @property
    def homogeneous_transform(self):
        return self._homogeneous_transform
    # If using homogeneous transform, the use the class below to get origin and reference frame:
    
    # THE BELOW IS WHAT MAKES THIS A SCENE GRPAH: nested drawing
    # FOR MULTIBODY DYNAMICS: scene graph will be 1-deep. that is, no VisFrame will 
    # have childrne. HOWEVER, this functionality could be useful in general for other users
    @property
    def child_frames(self):
        pass
    
    def child_frames_new(self, cframe): # or add_child_frame
        # cframe is any subclass of VisualizationFrame
        self._child_frames.append(cframe)
        
    def draw(self, transform):
        # draw your children, RELATIVE to this frame's transform. 
        
        # apply incoming transformation to MY transformation:
        transform = transform * self._homogeneous_transform
        
        for child in self._child_frames:
            child.draw(transform)
        # now draw shapes attached to THIS frame.
        for shape in self._shapes:
            shape.draw(transform)
        
        
    
class HomogeneousTransform(object):
    
    @property
    def origin(self):
        return matrix[0:2, 3]
    
    @property
    def rotation_matrix(self):
        return matrix[0:2, 0:2]
    
    
# I think in typical scene grpah imlementations, this has a more general superclass, like Drawable
class Shape(object):
    # Abstract base class
    __metaclass__ == abc.ABCMeta
    
    def __init__(self, name):
        pass
    
    def draw(self, homogeneous_transform):
        # Each shape needs to know how to draw itself, given an origin and a frame.
        pass
    
    def translate(self, position_vector):
        # Specify the frame in which the position_vector is expressed, and the point 
        # it gives the position from (origin given in homogeneous_transform)
        # functionalilty like this is crucial, because by default, say a cylinder
        # is drawn so its center is at the origin of the frame, but
        # we want to draw it so that its END is at the origin of the frame...
        pass
    
    def rotate(self, static_rotation_matrix, quaternion, euler_angles):
        # Preferably allow any general type of rotation specification here.
        # NOTE this rotation does NOT deal with dynamics, it's just orienting 
        # the shape in the frame to which it'll be attached.
        pass
    
class Rectangle(Shape):
    # etc.
    pass

class UserDefinedMesh(Shape):
    # accept OBJ file as input.
    pass

# Everything above has nothing to do with physics.mechanics. Everything 
# above should be super-general, maybe doesn't even depend on sympy if possible.
# Everything below DOES depend on physics.mechanics
class MultibodyDynamicsVisualizationFrame(VisualizationFrame):
    
    def __init__(self, rigid_body):
        Super(self, MultibodyDynamicsVisualizationFrame).__init__(rigid_body.name()) 
        self._rigid_body = rigid_body
        
    # below is more of what we want:
    @property
    def homogeneous_transform(self):
        return self._rigid_body.homogeneous_transform()
        
    # This class should not need to expose rigid_body (that is, there is no rigid_body property).
    

        
        


    
    
    
