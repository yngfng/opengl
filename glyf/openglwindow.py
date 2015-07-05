
import sys
from shaderProg import ShaderProgram
try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GL.ARB.shader_objects import *
    from OpenGL.GL.ARB.fragment_shader import *
    from OpenGL.GL.ARB.vertex_shader import *
    from glyf.mouseInteractor import MouseInteractor
except:
    print ''' Fehler: PyOpenGL nicht intalliert !!'''

    sys.exit(  )

frameRate = 25
time = 0.0

from time import sleep
def animationStep( ):
    """Update animated parameters."""
    global frameRate
    global time
    time+=0.05
    global sP
    if sP:
        glUseProgramObjectARB( 1L )
        glUniform1fARB( sP.indexOfUniformVariable("Time"), time )
    sleep( 1 / float( frameRate ) )
    glutPostRedisplay( )

def display(  ):
    """Glut display function."""
    if not torusList:
        init()
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glMatrixMode( GL_PROJECTION )
    glLoadIdentity( )
    xSize, ySize = glutGet( GLUT_WINDOW_WIDTH ), glutGet( GLUT_WINDOW_HEIGHT )
    gluPerspective(60, float(xSize) / float(ySize), 0.1, 50)
    glMatrixMode( GL_MODELVIEW )
    glLoadIdentity( )
    glTranslatef( 0, 0, -4 )
    glRotatef( 130, 1, 0, 0 )
    global mouseInteractor
    mouseInteractor.applyTransformation()

    glCallList( torusList )
    glutSwapBuffers( )

sP = None
def initShaders( ):
    """Initialise shaderProg object."""
    global sP
    sP = ShaderProgram( )
    sP.addShader( GL_VERTEX_SHADER_ARB, "brick.vert" )
    sP.addShader( GL_FRAGMENT_SHADER_ARB, "brick.frag" )
    sP.linkShaders( )
    sP.enable( )
    glUniform1fARB( sP.indexOfUniformVariable("Amplitude"), 0.1)
    glUniform3fvARB( sP.indexOfUniformVariable("LightPosition"), 1, \
        (0.0, 0.0, 3.0) )
    glUniform3fvARB( sP.indexOfUniformVariable("BrickColor"), 1, \
        (0.2, 0.3, 1.0) )
    glUniform3fvARB( sP.indexOfUniformVariable("MortarColor"), 1, \
        (0.85, 0.86, 0.84) )
    glUniform2fvARB( sP.indexOfUniformVariable("BrickSize"), 1, \
        (0.3, 0.15) )
    glUniform2fvARB( sP.indexOfUniformVariable("BrickPct"), 1, \
        (0.9, 0.85) )

torusList = None

def init(  ):
    "Glut init function."""
    glClearColor ( 0.3, 0.3, 0.3, 1 )
    glEnable( GL_DEPTH_TEST )
    glShadeModel( GL_SMOOTH )
    global mouseInteractor
    mouseInteractor = MouseInteractor(.01, 1)
    global torusList
    torusList = glGenLists( 1 )
    glNewList( torusList, GL_COMPILE )
    glutSolidTorus(0.5, 1, 40, 50);
    glEndList( )
    initShaders( )

def main():

    import logging
    logging.basicConfig()
    glutInit( sys.argv )
    glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH )
    glutInitWindowSize( 1550, 1250 )
    glutInitWindowPosition( 0, 0 )
    glutCreateWindow( sys.argv[0] )
    glutDisplayFunc( display )
    glutIdleFunc( animationStep )
    glutMainLoop(  )

if __name__ == "__main__":
    main()
    

