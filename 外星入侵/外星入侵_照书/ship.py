import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('C:\\Users\\jerry\\Documents\\GitHub\\Project\\外星入侵\\外星入侵_照书\\image\\飞船.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitime(self):
        self.screen.blit(self.image, self.rect)
