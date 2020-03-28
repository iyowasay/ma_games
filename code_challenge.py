from math import *
import pygame
import numpy as np

count = 0

size = (700, 700)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,128)
black = (0,0,0)


def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return sqrt(dx**2+dy**2)


def intersection(A, B, C, D):
    # line a
    a1 = B[1]-A[1]
    b1 = A[0]-B[0]
    c1 = a1*A[0]+b1*A[1]
    # line b
    a2 = D[1]-C[1]
    b2 = C[0]-D[0]
    c2 = a2*C[0]+b2*C[1]

    det = a1*b2-a2*b1
    if det == 0:
        return None
    else:
        inx = (b2*c1 - c2*b1) / det
        iny = (a1*c2 - c1*a2) / det
        t1, t2 = D[0]-C[0], inx-C[0]
        t3, t4 = C[1]-D[1], iny-D[1]
        if t1*t3 != 0 and (0 <= t2/t1 <= 1 or 0 <= t4/t3 <= 1):
            return [inx, iny]
        elif (t1 == 0 and 0 <= t4/t3 <= 1) or (t3 == 0 and 0 <= t2/t1 <= 1):
            return [inx, iny]
        else:
            return None


def m(sc, xx, yy, ww):
    big = 15
    pygame.draw.ellipse(sc, white, (xx-big/2, yy-big/2, big, big))
    for n in range(0, 360, 10):
        ex = xx + 2000 * cos(n * pi / 180)
        ey = yy + 2000 * sin(n * pi / 180)
        clo = list()
        pp = 100000
        for i in ww:
            temp = intersection((xx, yy), (ex, ey), i[0], i[1])
            if temp and distance(temp, [xx, yy]) <= pp and min(xx, ex) <= temp[0] <= max(xx, ex) and min(yy, ey) <= temp[1] <= max(yy, ey):
                pp = distance(temp, [xx, yy])
                clo = temp[:]

        if clo:
            pygame.draw.line(sc, white, (xx, yy), (clo[0], clo[1]))
        else:
            pygame.draw.line(sc, white, (xx, yy), (ex, ey))


def run_game():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('rayyyyyyy')
    np.random.seed()
    num_wall = 6
    wall_p1 = [(np.random.randint(675), np.random.randint(675)) for _ in range(num_wall)]
    wall_p2 = [(np.random.randint(675), np.random.randint(675)) for _ in range(num_wall)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        screen.fill(black)
        w_all = []

        for i in range(num_wall):
            w_all.append([wall_p1[i], wall_p2[i]])
            pygame.draw.line(screen, white, wall_p1[i], wall_p2[i], 4)

        mx, my = pygame.mouse.get_pos()
        m(screen, mx, my, w_all)
        pygame.display.flip()
        # pygame.display.update()
        # pygame.time.Clock().tick(15)


run_game()





