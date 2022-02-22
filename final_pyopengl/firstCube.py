import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


verticies = (
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1)
)

edges=(
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),#
    (2,7),#
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

surfaces=(
    (0,1,2,3),#
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

colors=(
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0)
)


def cube():
    #not only lines anymore
    glBegin(GL_QUADS)
    x=0
    for surface in surfaces:
        x += 1
        for vertex in surface:
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_LINES) #define gl
    #gl code that we want to specfy
    for edge in edges:
        for vertx in edge:
            glVertex3fv(verticies[vertx])
    glEnd()




def main():
    pygame.init() #need that every start
    display = (800,600)
    #double buffer - has buffer in the backgroung - not really understud
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    #fill the view - degries, ratio, and the cleeping plane and saprate the showing of the object
    gluPerspective(45, (display[0]/display[1]), 0.1,50.0)
    #x,y,z parameters - we want to be alittel far from the cubt - that why we give -5 in the z axis - zoom out
    glTranslatef(0.0,0.0,-10)
    glRotatef(0,0,0,0) #rotate acordding the axis x,y,z
    #run until the user click quit
    while True:
        #get every event
        for event in pygame.event.get():
            #exit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #keyboard event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-1, 0.0, 0.0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(1, 0.0, 0.0)
                if event.key == pygame.K_UP:
                    glTranslatef(0.0, 1, 0.0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0.0, -1, 0.0)
            #mouse event
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1)
                if event.button == 5:
                    glTranslatef(0,0,-1)
        glRotatef(1, 3, 1, 1)
        #clear the frame with something - clear all that specfiy
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube()
        #flipe is like update
        pygame.display.flip()
        pygame.time.wait(10)

main()