import OpenGL 
OpenGL.ERROR_ON_COPY = True 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL.shaders import *
from OpenGL.GL.ARB.shader_objects import *
from OpenGL.GL.ARB.fragment_shader import *
from OpenGL.GL.ARB.vertex_shader import *

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(640, 480)
    glutCreateWindow("Jeff Molofee's GL Code Tutorial ... NeHe '99")

    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(animationStep)
    glutReshapeFunc(ReSizeGLScene)

    InitGL(640, 480)
    glutMainLoop()

def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

	glEnable( GL_LIGHTING )
	glEnable( GL_LIGHT0 )
	glLightModeli( GL_LIGHT_MODEL_TWO_SIDE, 0 )
                glLightfv( GL_LIGHT0, GL_POSITION, [4, 4, 4, 1] )
	lA = 0.8,   glLightfv( GL_LIGHT0, GL_AMBIENT, [lA, lA, lA, 1] )
	lD = 1,     glLightfv( GL_LIGHT0, GL_DIFFUSE, [lD, lD, lD, 1] )
	lS = 1,     glLightfv( GL_LIGHT0, GL_SPECULAR, [lS, lS, lS, 1] )
	glMaterialfv( GL_FRONT_AND_BACK, GL_AMBIENT, [0.2, 0.2, 0.2, 1] )
	glMaterialfv( GL_FRONT_AND_BACK, GL_DIFFUSE, [0.7, 0.7, 0.7, 1] )
	glMaterialfv( GL_FRONT_AND_BACK, GL_SPECULAR, [0.5, 0.5, 0.5, 1] )
	glMaterialf( GL_FRONT_AND_BACK, GL_SHININESS, 50 )

    im = Image.open(fileName)
    xSize = im.size[0]
    ySize = im.size[1]
    rawReference = im.tostring("raw", "RGB", 0, -1)
	glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
	glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )
	glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
	glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
	glTexImage2D( GL_TEXTURE_2D, 0, 3, xSize, ySize, 0, GL_RGB, GL_UNSIGNED_BYTE, rawReference )
	glEnable( GL_TEXTURE_2D )

    torusList = glGenLists( 1 )
    glNewList( torusList, GL_COMPILE )
    glutSolidTorus(0.5, 1, 40, 50);
    glEndList( )

MENU_RED, MENU_GREEN, MENU_BLUE, MENU_QUIT = 0, 1, 2, 3
colors = [ [1, 0, 0], [0, 1, 0], [0, 0, 1] ]
def handleMenu( selection ):
	if selection == MENU_QUIT:
		sys.exit()
	elif MENU_RED <= selection <= MENU_BLUE:
		rP.drawColor = colors[ selection ]
	else:
		print 'Warning: illegel Menu entry'
	glutPostRedisplay( )

def initMenus( ):
	global handleMenu
	colorMenu = glutCreateMenu( handleMenu )
	glutAddMenuEntry( "red", MENU_RED )
	glutAddMenuEntry( "green", MENU_GREEN )
	glutAddMenuEntry( "blue", MENU_BLUE )
	glutCreateMenu( handleMenu )
	glutAddSubMenu( "color", colorMenu)
	glutAddMenuEntry( "quit", MENU_QUIT )
	glutAttachMenu( GLUT_RIGHT_BUTTON )


def initShaders( ):
    program = compileProgram( compileShader(''' ''',GL_VERTEX_SHADER), compileShader(''' ''',GL_FRAGMENT_SHADER),)
    glUseProgram(program)

    self.__shaderProgramID = glCreateProgramObjectARB()
    shaderHandle = glCreateShaderObjectARB(GL_FRAGMENT_SHADER_ARB)
    sourceString = open('brick.frag', 'r').read()
    glShaderSourceARB(shaderHandle, [sourceString] )
    glCompileShaderARB( shaderHandle )
    success = glGetObjectParameterivARB( shaderHandle, GL_OBJECT_COMPILE_STATUS_ARB)
    if (not success):
        print glGetInfoLogARB( shaderHandle )
        sys.exit( )
    glAttachObjectARB( self.__shaderProgramID, shaderHandle )
    glLinkProgramARB( self.__shaderProgramID )
    success = glGetObjectParameterivARB( self.__shaderProgramID, GL_OBJECT_LINK_STATUS_ARB )
    glUseProgramObjectARB( self.__shaderProgramID )
    glUniform1fARB( sP.indexOfUniformVariable("Amplitude"), 0.1)
    glUniform3fvARB( sP.indexOfUniformVariable("LightPosition"), 1, (0.0, 0.0, 3.0) )
    result = glGetAttribLocationARB( self.__shaderProgramID, attributeName )

    self.__shaderProgramID = glCreateProgramObjectARB()
        shaderHandle = glCreateShaderObjectARB(GL_FRAGMENT_SHADER_ARB)
            sourceString = open('brick.frag', 'r').read()
        glShaderSourceARB(shaderHandle, [sourceString] )
        glCompileShaderARB( shaderHandle )
    glAttachObjectARB( self.__shaderProgramID, shaderHandle )
    glLinkProgramARB( self.__shaderProgramID )
    glUseProgramObjectARB( self.__shaderProgramID )

	sP = ShaderProgram( )
	sP.addShader( GL_FRAGMENT_SHADER_ARB, "rgbMorph.frag" )
	sP.linkShaders( )
	sP.enable( )
	glUniformMatrix4fvARB(sP.indexOfUniformVariable("RGBTransformationMatrix"), 1, False, rgbTransformMatrix)

def ReSizeGLScene(Width, Height):
    if Height == 0: Height = 1
    #Width, Height = glutGet( GLUT_WINDOW_WIDTH ), glutGet( GLUT_WINDOW_HEIGHT )
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(-1.5, 0.0, -6.0)
    glRotatef( 130, 1, 0, 0 )
    glutSolidCube( 1.0 )
    glCallList( torusList )

	glColor3f( 1, 1, 1 )
	glBegin( GL_QUADS )
	glTexCoord2f( 0, 1 )
	glVertex3f( -0.5, 0.5, 0 )
	glTexCoord2f( 0, 0 )
	glVertex3f( -0.5, -0.5, 0 )
	glTexCoord2f( 1, 0 )
	glVertex3f( 0.5, -0.5, 0 )
	glTexCoord2f( 1, 1 )
	glVertex3f( 0.5, 0.5, 0 )
	glEnd(  )

    glutSwapBuffers()

from time import sleep
def animationStep( ):
    time+=0.05
    glUniform1fARB( sP.indexOfUniformVariable("Time"), time )
    sleep( 1 / float( frameRate ) )
    glutPostRedisplay( )

def keyPressed(*args):
    if args[0] == '\x1b':
        sys.exit()

