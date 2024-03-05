import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('platformer level editor')
clock = pygame.time.Clock()
selected_rect = 0
key_press = [False,0]


class Block:
    def __init__(self,num):
        self.rect = pygame.Rect((num % 12)*100, (num//12)*100, 100,100)
        self.type = 0
        self.num = num
    def update(self):
        pygame.draw.rect(screen, colour(self.type),self.rect)
        pygame.draw.rect(screen, ("black"),self.rect,2)


def colour(num):
    if num == 0:
        return ("#70a5d7")
    if num == 1:
        return ("#446482")
    if num == 2:
        return ("#bea925")
    if num in (3,4,5,6):
        return ("#824464")
    if num in (7,8):
        return ("black")
    if num == 9:
        return ('#6c25be')

def mous():
    global selected_rect
    mouse_pos = pygame.mouse.get_pos()
    selected_rect = mouse_pos[0]//100 + (mouse_pos[1] // 100) *12


num_list = []
for i in range(72):
    num_list.append(Block(i))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                print_list = []
                for i in num_list:
                    print_list.append(i.type)
                print(f"[{print_list}]")
            if int(event.key) in range(48, 58):
                key_press = [True,int(event.key)-48]
            else: print("keyboard issue")
        if event.type == pygame.KEYUP:
            key_press = [False,0]
            
            
    screen.fill("black")
    mous()
    if key_press[0]:
        num_list[selected_rect].type = key_press[1]
    for rect in num_list:
        rect.update()

    pygame.display.update()
    clock.tick(60)