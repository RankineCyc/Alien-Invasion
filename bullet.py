import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manages the bullet"""

    def __init__(self, ai_game):
        """Create a bullet object at ship current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet at (0, 0) and then set the position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet position as float
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet"""

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        "Draw the bullet"
        pygame.draw.rect(self.screen, self.color, self.rect)