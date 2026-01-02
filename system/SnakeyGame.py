import pygame # Import Statement! 
import random # Import Statement!

# setting up some initial parameters
WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20

pygame.font.init()
score_font = pygame.font.SysFont("poppins", 20)  # or any other font you'd like
score = 0

# color definition
WHITE = (255, 255, 255) # Original colors
RED = (255, 0, 0)
BLUE = (0, 0, 255) # ADDED NEW COLORS - Blue, Purple, Coral!
PURPLE = (51, 51, 255)
CORAL = (255, 102, 102)

# initialize pygame
pygame.init()

# setting up display
win = pygame.display.set_mode((WIDTH, HEIGHT))

# setting up clock
clock = pygame.time.Clock()

# snake and food initialization
snake_pos = [[WIDTH//2, HEIGHT//2]]
snake_speed = [0, BLOCK_SIZE]

teleport_walls = True  # set this to True to enable wall teleporting


def generate_food():
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE ) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE ) * BLOCK_SIZE
        food_pos = [x, y]
        if food_pos not in snake_pos:
            return food_pos
        
food_pos = generate_food()

def draw_objects():
    win.fill((0, 0, 0))
    for pos in snake_pos:
        pygame.draw.rect(win, CORAL, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(win, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
    # Render the score
    score_text = score_font.render(f"Your Score: {score}", True, BLUE)
    win.blit(score_text, (20, 20))  # draws the score on the top-left corner


def update_snake():
    global food_pos, score
    new_head = [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]]
    
    if teleport_walls:
        # if the new head position is outside of the screen, wrap it to the other side
        if new_head[0] >= WIDTH:
            new_head[0] = 0
        elif new_head[0] < 0:
            new_head[0] = WIDTH - BLOCK_SIZE
        if new_head[1] >= HEIGHT:
            new_head[1] = 0
        elif new_head[1] < 0:
            new_head[1] = HEIGHT - BLOCK_SIZE

    if new_head == food_pos:
        food_pos = generate_food() # generate new food
        score += 1  # increment score when food is eaten
    else:
        snake_pos.pop() # remove the last element from the snake
    
    snake_pos.insert(0, new_head) # add the new head to the snake


def game_over():
    # game over when snake hits the boundaries or runs into itself
    if teleport_walls:
        return snake_pos[0] in snake_pos[1:]
    else:
        return snake_pos[0] in snake_pos[1:] or \
            snake_pos[0][0] > WIDTH - BLOCK_SIZE or \
            snake_pos[0][0] < 0 or \
            snake_pos[0][1] > HEIGHT - BLOCK_SIZE or \
            snake_pos[0][1] < 0


def game_over_screen():
    global score
    win.fill((0, 0, 0))
    game_over_font = pygame.font.SysFont("poppins", 50)
    game_over_text = game_over_font.render(f"GAME OVER! Your Final Score: {score}", True, PURPLE)
    win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run()  # replay the game to (bind key to r)
                    return
                elif event.key == pygame.K_q:
                    pygame.quit()  # quit the game (bind key to q)
                    return



def run():
    global snake_speed, snake_pos, food_pos, score
    snake_pos = [[WIDTH//2, HEIGHT//2]]
    snake_speed = [0, BLOCK_SIZE]
    food_pos = generate_food()
    score = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_UP]:
                    # when UP is pressed but the snake is moving down, ignore the input.
                    if snake_speed[1] == BLOCK_SIZE:
                        continue
                    snake_speed = [0, -BLOCK_SIZE]
                if keys[pygame.K_DOWN]:
                    # when DOWN is pressed but the snake is moving up, ignore the input.
                    if snake_speed[1] == -BLOCK_SIZE:
                        continue
                    snake_speed = [0, BLOCK_SIZE]
                if keys[pygame.K_LEFT]:
                    # when LEFT is pressed but the snake is moving right, ignore the input.
                    if snake_speed[0] == BLOCK_SIZE:
                        continue
                    snake_speed = [-BLOCK_SIZE, 0]
                if keys[pygame.K_RIGHT]:
                    # when RIGHT is pressed but the snake is moving left, ignore the input.
                    if snake_speed[0] == -BLOCK_SIZE:
                        continue
                    snake_speed = [BLOCK_SIZE, 0]

        draw_objects()
        update_snake()
        if game_over():
            game_over_screen()
            break
        pygame.display.update()
        clock.tick(12) # TO set speed
    pygame.quit() # To quit using key Q


if __name__ == '__main__':
    run()
