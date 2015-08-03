import pygame


class GameObj(pygame.sprite.Sprite):

    def __init__(self, x, y, image=None):
        super().__init__()
        if image:
            self.image             = pygame.image.load(image).convert_alpha()
            self.rect              = self.image.get_rect()
            self.rect.x            = x
            self.rect.y            = y

    def _collide_with_blocks_x(self):
        # Did this update cause us to hit a wall?
        blocks_hit = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in blocks_hit:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.velX > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

    def _collide_with_blocks_y(self):
        # Check and see if we hit anything
        blocks_hit = pygame.sprite.spritecollide(self, self.blocks, False)
        for block in blocks_hit:
 
            # Reset our position based on the top/bottom of the object.
            if self.velY > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom