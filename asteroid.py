import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        spawn_angle = random.uniform(20, 50)
        first_spawn = Asteroid(
            self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS
        )
        first_spawn.velocity = self.velocity.rotate(spawn_angle) * 1.2
        second_spawn = Asteroid(
            self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS
        )
        second_spawn.velocity = self.velocity.rotate(-spawn_angle) * 1.2
