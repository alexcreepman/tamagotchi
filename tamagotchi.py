from pet import Pet
import pygame.freetype
import argparse

parser = argparse.ArgumentParser(description='Game settings.')
parser.add_argument('--fps', type=int, default=24,
                    help='framerate')  # for a movie-like like experience
parser.add_argument('--width', type=int, default=854,
                    help='screen width')
parser.add_argument('--height', type=int, default=480,
                    help='screen height')
# you're watching the movie on a cellphone with 3g btw
parser.add_argument('--name', type=str, default="Keith",  # кiт по имени Кiт
                    help="pet's name")

args = parser.parse_args()
FPS = args.fps
SCREEN_WIDTH = args.width
SCREEN_HEIGHT = args.height
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WHITISH = (200, 200, 200)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Tamagotchi")
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.freetype.Font('font.ttf', SCREEN_HEIGHT / 16)
bg = pygame.image.load("graphics/bg.jpg")
# name = input("Name your pet: ")
p = Pet(args.name)
pygame.display.set_caption(args.name)
game_loop_status = True
cur_frame = 0
while game_loop_status:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop_status = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if SCREEN_WIDTH / 10 <= mouse[
                0] <= 35 * SCREEN_WIDTH / 100 and (4 * SCREEN_HEIGHT / 5 <=
                                                   mouse[1] <=
                                                   9 * SCREEN_HEIGHT / 10):
                p.play()
            elif 4 * SCREEN_WIDTH / 10 <= mouse[
                0] <= 65 * SCREEN_WIDTH / 100 and (4 * SCREEN_HEIGHT / 5 <=
                                                   mouse[1] <=
                                                   9 * SCREEN_HEIGHT / 10):
                p.feed()
            elif 7 * SCREEN_WIDTH / 10 <= mouse[
                0] <= 95 * SCREEN_WIDTH / 100 and (4 * SCREEN_HEIGHT / 5 <=
                                                   mouse[1] <=
                                                   9 * SCREEN_HEIGHT / 10):
                game_loop_status = False
    clock.tick(FPS)
    cur_frame += 1
    if cur_frame >= FPS:
        p.tick()
        cur_frame = 0
    screen.fill(BLACK)
    screen.blit(bg, [0, 0])
    pet_sprite = pygame.image.load(p.get_status())
    half_screen = 2 * min(SCREEN_HEIGHT, SCREEN_WIDTH) // 3
    pet_sprite = pygame.transform.scale(pet_sprite, (half_screen, half_screen))
    screen.blit(pet_sprite, [SCREEN_WIDTH // 20, SCREEN_HEIGHT // 20])
    font.render_to(screen, (23 * SCREEN_WIDTH / 40, 3 * SCREEN_HEIGHT / 40),
                   p.name.upper() + p.is_dead(), WHITISH)

    pygame.draw.rect(screen, BLACK, [half_screen + SCREEN_WIDTH // 10,
                                     7 * SCREEN_HEIGHT // 40,
                                     SCREEN_WIDTH // 3,
                                     SCREEN_HEIGHT // 10])
    pygame.draw.rect(screen, RED, [half_screen + SCREEN_WIDTH // 10,
                                   7 * SCREEN_HEIGHT // 40,
                                   p.chonkiness * SCREEN_WIDTH //
                                   (3 * p.chonk_cap),
                                   SCREEN_HEIGHT // 10])
    font.render_to(screen, (half_screen + 5 * SCREEN_WIDTH // 40,
                            8 * SCREEN_HEIGHT / 40),
                   "CHONKINESS", WHITISH)
    pygame.draw.rect(screen, BLACK, [half_screen + SCREEN_WIDTH // 10,
                                     12 * SCREEN_HEIGHT // 40,
                                     SCREEN_WIDTH // 3,
                                     SCREEN_HEIGHT // 10])
    pygame.draw.rect(screen, BLUE, [half_screen + SCREEN_WIDTH // 10,
                                    12 * SCREEN_HEIGHT // 40,
                                    p.joy * SCREEN_WIDTH //
                                    (3 * p.joy_cap),
                                    SCREEN_HEIGHT // 10])
    font.render_to(screen, (half_screen + 5 * SCREEN_WIDTH // 40,
                            13 * SCREEN_HEIGHT / 40),
                   "JOY", WHITISH)
    pygame.draw.rect(screen, WHITISH, [SCREEN_WIDTH / 10,
                                       4 * SCREEN_HEIGHT / 5,
                                       SCREEN_WIDTH / 4,
                                       SCREEN_HEIGHT / 10])
    font.render_to(screen, (7 * SCREEN_WIDTH / 40, 33 * SCREEN_HEIGHT / 40),
                   "PLAY", BLACK)

    pygame.draw.rect(screen, WHITISH, [4 * SCREEN_WIDTH / 10,
                                       4 * SCREEN_HEIGHT / 5,
                                       SCREEN_WIDTH / 4,
                                       SCREEN_HEIGHT / 10])
    font.render_to(screen, (19 * SCREEN_WIDTH / 40, 33 * SCREEN_HEIGHT / 40),
                   "FEED", BLACK)
    pygame.draw.rect(screen, WHITISH, [7 * SCREEN_WIDTH / 10,
                                       4 * SCREEN_HEIGHT / 5,
                                       SCREEN_WIDTH / 4,
                                       SCREEN_HEIGHT / 10])
    font.render_to(screen, (31 * SCREEN_WIDTH / 40, 33 * SCREEN_HEIGHT / 40),
                   "QUIT", BLACK)

    pygame.display.flip()
pygame.quit()
