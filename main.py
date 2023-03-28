import pygame
import random
pygame.init()
tick = 60
width_height = (900,800)
colors1 = [(255,0,0), (0,150,0)]
button_hh = (50,100)
step = 14
font_size = 20
font_size_label = 50
my_list_button = list()
clock = pygame.time.Clock()
win = pygame.display.set_mode(width_height)
list_colors = [(242, 230, 0),(255,0,0),(38, 52, 0),(0,150,0),(182, 165, 214),(155,0,0),(0,250,0),(250,0,0)]
pygame.display.set_caption("Игра Цвиточек")
class Area():#2022
    def __init__(self,x = None,y = None,width = None,height = None,color = list_colors[0],):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.COLOR = color
        self.COLOR2 = random.choice(colors1)
        self.rectanglle = pygame.Rect(self.X,self.Y,self.WIDTH,self.HEIGHT)
        self.SELECT = False
        self.FONT = pygame.font.Font(None,font_size)
    def blit_button(self,win):
        pygame.draw.rect(win, self.COLOR, self.rectanglle)
        pygame.draw.rect(win, list_colors[2], self.rectanglle, width = 4)
        if self.SELECT:
            pygame.draw.rect(win, self.COLOR2, self.rectanglle)
            pygame.draw.rect(win, list_colors[2], self.rectanglle, width=4)
class text:
    def __init__(self,x = width_height[0] - font_size_label * 10,y  = font_size_label ):
        self.X = x
        self.Y = y
        self.FONT = pygame.font.Font(None,font_size_label)
        self.SCORE = 15
        self.TEXT = self.FONT.render('ТАЙМЕР: ' + str(self.SCORE), True, list_colors[3])
    def blit_text(self,win):
        self.TEXT = self.FONT.render('ТАЙМЕР: ' + str(self.SCORE), True, list_colors[3])
        win.blit(self.TEXT,(self.X,self.Y))
def create_rect(count):
    x = width_height[0] // 2 - (button_hh[0] + step) * count/2
    y = width_height[1] // 2 - button_hh[1] // 2
    for el in range(count):
        button = Area(x = x, y = y, width= button_hh[0], height = button_hh[1])
        my_list_button.append(button)
        x += button_hh[0] + step
count3 = 3
create_rect(count3)
def run_game():
    game = True
    count_button_select = 0
    count_color = 0
    score = text()
    while game:
        win.fill(list_colors[4])
        if count_color == 0:
            for button in my_list_button:
                button.COLOR = list_colors[0]
            count_color = -1
        else:
            count_color -= 1
        if count_button_select == 0:
            for button in my_list_button:
                if button.SELECT:
                    button.SELECT = False
                    score.SCORE -= 1
            random_index = random.randint(0, len(my_list_button) - 1)
            my_list_button[random_index].SELECT = True
            count_button_select = 60
        else:
            count_button_select -= 1
        score.blit_text(win)
        for button in my_list_button:
            button.blit_button(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                for button in my_list_button:
                    if button.rectanglle.collidepoint(x,y):
                        if button.SELECT:
                            if button.COLOR2 == colors1[0]:
                                if len(my_list_button) == 1:
                                    game = False
                                    print("Ты победил!")
                                elif len(my_list_button) == 2:
                                    list.clear(my_list_button)
                                    create_rect(count3 - 2)
                                elif len(my_list_button) == 3:
                                    list.clear(my_list_button)
                                    create_rect(count3 - 1)
                                elif len(my_list_button) == 4:
                                    list.clear(my_list_button)
                                    create_rect(count3)
                                elif len(my_list_button) == 5:
                                    list.clear(my_list_button)
                                    create_rect(count3 + 1)
                                elif len(my_list_button) == 6:
                                    list.clear(my_list_button)
                                    create_rect(count3 + 2)
                                elif len(my_list_button) == 7:
                                    list.clear(my_list_button)
                                    create_rect(count3 + 3)
                                elif len(my_list_button) == 8:
                                    list.clear(my_list_button)
                                    create_rect(count3 + 4)
                                elif len(my_list_button) == 9:
                                    list.clear(my_list_button)
                                    create_rect(count3 + 5)
                                elif len(my_list_button) == 10:
                                    game = False
                                    print("Ф")
                            elif button.COLOR2 == colors1[1]:
                                if len(my_list_button) == 1:
                                    list.clear(my_list_button)
                                    create_rect(count3 - 1)
                                elif len(my_list_button) == 2:
                                    list.clear(my_list_button)
                                    create_rect(count3)
                                elif len(my_list_button) == 3:
                                    list.clear(my_list_button)
                                    create_rect(count3 + 1)
                                elif len(my_list_button) == 4:
                                    list.clear(my_list_button)
                                    create_rect(count3 + 2)
                                elif len(my_list_button) == 5:
                                    list.clear(my_list_button)
                                    create_rect(count3 + 3)
                                elif len(my_list_button) == 6:
                                    list.clear(my_list_button)
                                    create_rect(count3 + 4)
                                elif len(my_list_button) == 7:
                                    list.clear(my_list_button)
                                    create_rect(count3 + 5)
                                elif len(my_list_button) == 8:
                                    list.clear(my_list_button)
                                    create_rect(count3 + 6)
                                elif len(my_list_button) == 9:
                                    list.clear(my_list_button)
                                    create_rect(count3 + 7)
                                elif len(my_list_button) == 10:
                                    game = False
                                    print("Ты проиграл!")
                        else:
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                x, y = event.pos
                                for button in my_list_button:
                                    if button.rectanglle.collidepoint(x, y):
                                            if button.COLOR2 != colors1[0] or button.COLOR2 != colors1[1]:
                                                game = False
                        count_color = 60
                        button.SELECT = False
        if score.SCORE == 0:
            game = False
            print("Ты, проиграл")
        clock.tick(tick)
        pygame.display.flip()
run_game()
