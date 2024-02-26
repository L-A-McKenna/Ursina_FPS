from ursina import Entity, color, destroy, random

def create_enemy(position):
    return Entity(model='cube', color=color.blue, scale=(0.5, 1, 0.5), position=position, collider='box')