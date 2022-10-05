import pygame
import spritesheet
pygame.init()
# Window & caption
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First game")


# Load sprite sheet
sprite_image = pygame.image.load('DinoSprites - doux.png').convert_alpha()

sprite_sheet = spritesheet.SpriteSheet(sprite_image)

# Sprite Width, Height, & scale
sprite_image_width = 24
sprite_image_height = 24
sprite_image_scale = 4

# Tranparency for Sprite
BLACK = (0, 0, 0)

# Create sprite lists
animation_list = []
animation_steps = [4, 6, 3, 4]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 75
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, sprite_image_width, sprite_image_height, sprite_image_scale, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)


screen_Width = 500

x = 50
y = 400
width = 40
height = 60
vel = 10
fps = 50

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # side to side / up and down movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > vel:
        x -= vel

    if keys[pygame.K_d] and x < screen_Width - width - vel:
        x += vel

    # Jumping
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True  
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1          
        else:
            isJump = False
            jumpCount = 10
    win.fill((50,50,50))

    # Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0
    # Show frame image
    win.blit(animation_list[action][frame], (x, y))
    pygame.display.update()
pygame.quit
