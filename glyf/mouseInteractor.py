# helper class for mouse interaction
# 
# Copyright (C) 2007  "Peter Roesch" <Peter.Roesch@fh-augsburg.de>
#
# This code is licensed under the PyOpenGL License.
# Details are given in the file license.txt included in this distribution.

import sys
import math

from interactionMatrix import InteractionMatrix

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ''' Error: PyOpenGL not installed properly !!'''
  sys.exit(  )

class MouseInteractor ( object ):
    """Connection between mouse motion and transformation matrix"""
    def __init__( self, translationScale=0.1, rotationScale=.2):
        self.scalingFactorRotation = rotationScale
        self.scalingFactorTranslation = translationScale
        self.rotationMatrix = InteractionMatrix( )
        self.translationMatrix = InteractionMatrix( )
        self.mouseButtonPressed = 'rot'
        self.oldMousePos = [ 0, 0 ]
        self.registerCallbacks()

    def mouseButton( self, button, mode, x, y ):
        """Callback function for mouse button."""
        self.oldMousePos[0], self.oldMousePos[1] = x, y
        glutPostRedisplay( )

    def mouseMotion( self, x, y ):
        """Callback function for mouse motion.

        Depending on the button pressed, the displacement of the
        mouse pointer is either converted into a translation vector
        or a rotation matrix."""

        deltaX = x - self.oldMousePos[ 0 ]
        deltaY = y - self.oldMousePos[ 1 ]
        if self.mouseButtonPressed == 'scale':
            tX = deltaX * self.scalingFactorTranslation
            tY = deltaY * self.scalingFactorTranslation
            self.translationMatrix.addTranslation(tX, -tY, 0)
        elif self.mouseButtonPressed == 'rot':
            rY = deltaX * self.scalingFactorRotation
            self.rotationMatrix.addRotation(rY, 0, 1, 0)
            rX = deltaY * self.scalingFactorRotation
            self.rotationMatrix.addRotation(rX, 1, 0, 0)
        if self.mouseButtonPressed == 'zoom':
            tZ = deltaY * self.scalingFactorTranslation
            self.translationMatrix.addTranslation(0, 0, tZ)
        self.oldMousePos[0], self.oldMousePos[1] = x, y
        glutPostRedisplay( )

    # change view angle, exit upon ESC
    def keyFunc(self, k, x, y):
        if k == 's':
            self.mouseButtonPressed = 'scale'
        elif k == 'a':
            self.mouseButtonPressed = 'rot'
        elif k == 'z':
            self.mouseButtonPressed = 'zoom'
        elif k == 'x':
            self.mouseButtonPressed = None
        elif ord(k) == 27 or k == 'q': # Escape
            sys.exit(0)
        else:
            return
        glutPostRedisplay()

    def applyTransformation( self ):
        """Concatenation of the current translation and rotation
        matrices with the current OpenGL transformation matrix"""

        glMultMatrixf( self.translationMatrix.getCurrentMatrix() )
        glMultMatrixf( self.rotationMatrix.getCurrentMatrix() )

    def registerCallbacks( self ):
        """Initialise glut callback functions."""
        glutMouseFunc( self.mouseButton )
        glutMotionFunc( self.mouseMotion )
        glutKeyboardFunc( self.keyFunc )

