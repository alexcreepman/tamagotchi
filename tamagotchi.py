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

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Tamagotchi")
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.freetype.Font('font.ttf', SCREEN_HEIGHT / 16)

# name = input("Name your pet: ")
p = Pet(args.name)
pygame.display.set_caption(args.name)
game_loop_status = True
curframe = 0
while game_loop_status:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop_status = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if SCREEN_WIDTH / 10 <= mouse[
                0] <= 35 * SCREEN_WIDTH / 100 and (4 * SCREEN_HEIGHT / 5 <=
                    mouse[1] <= 9 * SCREEN_HEIGHT / 10):
                        p.play()
            elif 4 * SCREEN_WIDTH / 10 <= mouse[
                0] <= 65 * SCREEN_WIDTH / 100 and (4 * SCREEN_HEIGHT / 5 <=
                    mouse[1] <= 9 * SCREEN_HEIGHT / 10):
                        p.feed()
            elif 7 * SCREEN_WIDTH / 10 <= mouse[
                0] <= 95 * SCREEN_WIDTH / 100 and (4 * SCREEN_HEIGHT / 5 <=
                    mouse[1] <= 9 * SCREEN_HEIGHT / 10):
                        game_loop_status = False

    clock.tick(FPS)
    curframe += 1
    if curframe >= FPS:
        p.tick()
        curframe = 0
    screen.fill((0, 0, 0))
    i = 0
    wordHeight = font.get_sized_glyph_height(0)
    for line in p.getStatus():
        font.render_to(screen, (0, i * wordHeight), line, (255, 255, 255))
        i += 1
    pygame.draw.rect(screen, (200, 200, 200), [SCREEN_WIDTH / 10,
                                               4 * SCREEN_HEIGHT / 5,
                                               SCREEN_WIDTH / 4,
                                               SCREEN_HEIGHT / 10])
    font.render_to(screen, (7 * SCREEN_WIDTH / 40, 33 * SCREEN_HEIGHT / 40),
                   "PLAY", (0, 0, 0))

    pygame.draw.rect(screen, (200, 200, 200), [4 * SCREEN_WIDTH / 10,
                                               4 * SCREEN_HEIGHT / 5,
                                               SCREEN_WIDTH / 4,
                                               SCREEN_HEIGHT / 10])
    font.render_to(screen, (19 * SCREEN_WIDTH / 40, 33 * SCREEN_HEIGHT / 40),
                   "FEED", (0, 0, 0))
    pygame.draw.rect(screen, (200, 200, 200), [7 * SCREEN_WIDTH / 10,
                                               4 * SCREEN_HEIGHT / 5,
                                               SCREEN_WIDTH / 4,
                                               SCREEN_HEIGHT / 10])
    font.render_to(screen, (31 * SCREEN_WIDTH / 40, 33 * SCREEN_HEIGHT / 40),
                   "QUIT", (0, 0, 0))
    pygame.display.flip()
pygame.quit()
