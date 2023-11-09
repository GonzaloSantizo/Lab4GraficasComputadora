import pygame
from pygame.locals import *
import glm
from gl import Renderer
from model import Model
from shaders import *
from obj import Obj

width = 500
height = 400

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

# Asumiendo que tienes las funciones setShader y useShader correctamente definidas en tu Renderer
rend = Renderer(screen)
rend.setShader(vertex_shader, fragmet_shader)

obj = Obj("bird.obj")
renderx = Model(obj.assemble())
renderx.loadTexture("bird.jpg")
renderx.position.z = -8
renderx.scale = glm.vec3(0.3,0.3,0.3)
renderx.rotation = glm.vec3(0,0,0)

rend.scene.append(renderx)
rend.target = renderx.position

isRunning = True
while isRunning:
    deltaTime = clock.tick(60) / 1000
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            elif event.key == pygame.K_SPACE:
                rend.toggleFilledMode()
            elif event.key == pygame.K_1:
             
                rend.setShader(vertex_shader2, fragmet_shader1)
            elif event.key == pygame.K_2:
                
                rend.setShader(vertex_shader1, fragmet_shader2)

            elif event.key == pygame.K_3:
                
                rend.setShader(vertex_shader3, fragmet_shader3)

    if keys[K_a]:
        rend.camPosition.x += 5 * deltaTime
    elif keys[K_d]:
        rend.camPosition.x -= 5 * deltaTime

    if keys[K_w]:
        rend.camPosition.y += 5 * deltaTime
    elif keys[K_s]:
        rend.camPosition.y -= 5 * deltaTime

    if keys[K_q]:
        rend.camPosition.z += 5 * deltaTime
    elif keys[K_e]:
        rend.camPosition.z -= 5 * deltaTime

    # Actualiza la rotación del modelo si se desea
    # renderx.rotation.y += 45 * deltaTime

    rend.elapsedTime += deltaTime

    rend.update()
    rend.render()

    pygame.display.flip()

pygame.quit()
