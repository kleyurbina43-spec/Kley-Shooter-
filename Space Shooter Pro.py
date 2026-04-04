import pygame
import random
import sys

# Inicializar
pygame.init()

# Pantalla completa
info = pygame.display.Info()
ANCHO, ALTO = info.current_w, info.current_h
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Colores
NEGRO = (5, 5, 10)
AMARILLO = (255, 255, 0)
VERDE_NEON = (57, 255, 20)
ROJO_FUERTE = (255, 0, 50)
BLANCO = (255, 255, 255)

# --- AJUSTES PARA 60 FPS ---
FPS = 60
velocidad_nave = 0.2 # Sensibilidad de suavizado
enemigo_vel_inicial = 8
bala_vel = -35 

# Jugador
j_ancho = 120
j_alto = 80
jugador_x = ANCHO // 2
jugador_y = ALTO - 250

# Estrellas (Efecto de fondo)
estrellas = [[random.randint(0, ANCHO), random.randint(0, ALTO)] for _ in range(50)]

# Objetos
balas = []
enemigos = []
puntos = 0
vidas = 3

def crear_enemigo():
    radio = random.randint(40, 70)
    x = random.randint(radio, ANCHO - radio)
    # Velocidad aleatoria ligeramente distinta para cada enemigo
    v = enemigo_vel_inicial + random.uniform(0, 4)
    return [x, -radio, radio, v]

# Población inicial
for _ in range(6):
    enemigos.append(crear_enemigo())

reloj = pygame.time.Clock()
cadencia = 0

# --- BUCLE PRINCIPAL ---
while vidas > 0:
    ventana.fill(NEGRO)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEMOTION:
            # Suavizado de movimiento: la nave sigue al dedo
            jugador_x = evento.pos[0] - j_ancho // 2

    # Dibujar Estrellas (Parallax simple)
    for estrella in estrellas:
        estrella[1] += 2
        if estrella[1] > ALTO: estrella[1] = 0
        pygame.draw.circle(ventana, (100, 100, 100), estrella, 2)

    # Disparo automático (ajustado a 60 FPS)
    cadencia += 1
    if cadencia % 8 == 0: # Dispara cada 8 frames
        balas.append([jugador_x + j_ancho // 2, jugador_y])

    # Lógica de Balas
    for b in balas[:]:
        b[1] += bala_vel
        if b[1] < -50:
            balas.remove(b)
        else:
            pygame.draw.rect(ventana, AMARILLO, (b[0]-6, b[1], 12, 40))

    # Lógica de Enemigos
    for e in enemigos[:]:
        e[1] += e[3] # Usar su velocidad individual
        
        # Dibujar enemigo con un borde para que se vea mejor
        pygame.draw.circle(ventana, ROJO_FUERTE, (int(e[0]), int(e[1])), e[2])
        pygame.draw.circle(ventana, BLANCO, (int(e[0]), int(e[1])), e[2], 3)
        
        # Colisiones
        for b in balas[:]:
            dist = ((e[0]-b[0])**2 + (e[1]-b[1])**2)**0.5
            if dist < e[2]:
                if e in enemigos: enemigos.remove(e)
                if b in balas: balas.remove(b)
                enemigos.append(crear_enemigo())
                puntos += 1
                # Dificultad incremental
                if puntos % 5 == 0: 
                    enemigo_vel_inicial += 0.1

        # Perder vida
        if e[1] > ALTO + e[2]:
            enemigos.remove(e)
            enemigos.append(crear_enemigo())
            vidas -= 1
        elif (jugador_x < e[0] < jugador_x + j_ancho) and \
             (jugador_y < e[1] < jugador_y + j_alto):
            enemigos.remove(e)
            enemigos.append(crear_enemigo())
            vidas -= 1

    # Dibujar Nave
    pygame.draw.rect(ventana, VERDE_NEON, (jugador_x, jugador_y, j_ancho, j_alto), border_radius=10)
    pygame.draw.polygon(ventana, BLANCO, [
        (jugador_x + 20, jugador_y), 
        (jugador_x + j_ancho - 20, jugador_y), 
        (jugador_x + j_ancho//2, jugador_y - 40)
    ])

    # UI Modernizada
    fuente = pygame.font.SysFont("sans-serif", 70, bold=True)
    sur_puntos = fuente.render(f"{puntos}", True, BLANCO)
    sur_vidas = fuente.render("♥" * vidas, True, ROJO_FUERTE)
    
    ventana.blit(sur_puntos, (ANCHO // 2 - 20, 50))
    ventana.blit(sur_vidas, (50, 50))

    pygame.display.flip() # flip() es a veces más eficiente que update()
    reloj.tick(FPS) # <--- AQUÍ SE SETEAN LOS 60 FPS

print(f"Puntuación final: {puntos}")
