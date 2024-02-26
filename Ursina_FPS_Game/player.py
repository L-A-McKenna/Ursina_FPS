from ursina.prefabs.first_person_controller import FirstPersonController

def create_player():
    return FirstPersonController(position=(0, 1, 0), collider='box')