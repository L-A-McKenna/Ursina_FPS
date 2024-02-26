from ursina import Entity, color, destroy, invoke, curve, time

def create_bullet(player, bullets):
    bullet = Entity(model='cube', color=color.red, scale=(0.1, 0.1, 0.5),
                    position=player.position + player.up + player.forward, rotation=player.rotation, collider='box')
    bullet.animate_position(bullet.position + bullet.forward * 10, duration=1, curve=curve.linear)
    bullets.append(bullet)
    invoke(destroy, bullet, delay=5)