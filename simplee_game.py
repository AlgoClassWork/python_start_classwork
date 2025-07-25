import pygame
from time import time

# Инициализация Pygame
pygame.init()
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Игра: убеги от врага")

# Установка кадров в секунду
clock = pygame.time.Clock()
FPS = 60

# Шрифты
font_big = pygame.font.SysFont('Arial', 70)
font_small = pygame.font.SysFont('Arial', 30)

# Загрузка изображений
background = pygame.transform.scale(pygame.image.load('back.jpg'), (700, 500))
player_image = pygame.transform.scale(pygame.image.load('pica.png'), (100, 100))
enemy_image = pygame.transform.scale(pygame.image.load('pica.png'), (100, 100))

# Начальные позиции
player_x, player_y = 200, 200
enemy_x, enemy_y = 400, 200

# Состояние игры
game_over = False
win = False
start_time = time()

# Основной цикл
running = True
while running:
    clock.tick(FPS)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Логика игры
    if not game_over:
        # Движение игрока
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player_y > 0:
            player_y -= 3
        if keys[pygame.K_s] and player_y < 400:
            player_y += 3
        if keys[pygame.K_a] and player_x > 0:
            player_x -= 3
        if keys[pygame.K_d] and player_x < 600:
            player_x += 3

        # Движение врага к игроку
        if enemy_x < player_x:
            enemy_x += 1
        elif enemy_x > player_x:
            enemy_x -= 1

        if enemy_y < player_y:
            enemy_y += 1
        elif enemy_y > player_y:
            enemy_y -= 1

        # Проверка столкновения
        player_rect = pygame.Rect(player_x, player_y, 100, 100)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, 100, 100)
        if player_rect.colliderect(enemy_rect):
            game_over = True
            win = False

        # Проверка победы по времени
        elapsed_time = int(time() - start_time)
        if elapsed_time >= 20:
            game_over = True
            win = True
    else:
        # Время останавливаем, чтобы не тикало дальше
        elapsed_time = int(time() - start_time)

    # Отрисовка
    window.blit(background, (0, 0))
    window.blit(player_image, (player_x, player_y))
    window.blit(enemy_image, (enemy_x, enemy_y))

    # Отображение времени
    timer_text = font_small.render(f"Время: {elapsed_time}", True, (255, 255, 255))
    window.blit(timer_text, (10, 10))

    # Если игра окончена, выводим сообщение
    if game_over:
        if win:
            result_text = font_big.render("Ты победил!", True, (0, 255, 0))
        else:
            result_text = font_big.render("Ты проиграл", True, (255, 0, 0))
        window.blit(result_text, (150, 200))

    pygame.display.update()

pygame.quit()
