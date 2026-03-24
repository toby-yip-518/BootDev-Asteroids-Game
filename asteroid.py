import random
from circleshape import *
from constants import *
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20,50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_second = Asteroid(self.position.x, self.position.y, new_radius)

        first_rotate = self.velocity.rotate(random_angle)
        second_rotate = self.velocity.rotate(-random_angle)

        new_asteroid_one.velocity = first_rotate * 1.2
        new_asteroid_second.velocity = second_rotate * 1.2