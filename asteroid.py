import pygame
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,
                           self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        randAngle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(randAngle)
        velocity2 = self.velocity.rotate(-randAngle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position[0], self.position[1],
                 newRadius).velocity = velocity1 * 1.2
        Asteroid(self.position[0], self.position[1],
                 newRadius).velocity = velocity2 * 1.2
