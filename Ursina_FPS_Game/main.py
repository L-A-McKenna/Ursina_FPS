from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from player import create_player
from enemy import create_enemy
from bullet import create_bullet

app = Ursina()

# Parameters
ground_size = 20
player_height = 1
enemy_spawn_interval = 2.0  # in seconds
max_enemies = 5  # Maximum number of enemies
score = 0

# Create entities
ground = Entity(model='plane', scale=(ground_size, 1, ground_size),
                color=color.green.tint(0.8), texture='white_cube', collider='box')
player = create_player()

enemies = []
bullets = []
enemies_to_destroy = []

score_text = Text(text=f"Score: {score}", y=-0.45, origin=(0, 0), scale=2)

def update():
    global score

    # Enemy spawning
    if len(enemies) < max_enemies and time.time() % enemy_spawn_interval < 0.1:
        enemy_position = (random.uniform(-ground_size/2, ground_size/2), player_height, random.uniform(-ground_size/2, ground_size/2))
        enemy = create_enemy(enemy_position)
        enemies.append(enemy)

    # Check for collisions with enemies
    for enemy in enemies:
        if player.intersects(enemy).hit:
            enemies_to_destroy.append(enemy)
            score -= 1

    # Destroy enemies marked for destruction
    for enemy in enemies_to_destroy:
        enemies.remove(enemy)
        destroy(enemy)
    enemies_to_destroy.clear()

    # Check for collisions with bullets
    for bullet in bullets.copy():
        for enemy in enemies:
            if bullet.intersects(enemy).hit:
                bullets.remove(bullet)
                enemies_to_destroy.append(enemy)
                score += 1

    # Update score
    score_text.text = f"Score: {score}"

def input(key):
    if key == 'left mouse down':
        create_bullet(player, bullets)

app.run()