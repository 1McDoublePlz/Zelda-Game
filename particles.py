import pygame
from support import import_folder
from random import choice

class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # magic
            'flame': import_folder('1 - level/graphics/particles/flame/frames'),
            'aura': import_folder('1 - level/graphics/particles/aura'),
            'heal': import_folder('1 - level/graphics/particles/heal/frames'),
            
            # attacks 
            'claw': import_folder('1 - level/graphics/particles/claw'),
            'slash': import_folder('1 - level/graphics/particles/slash'),
            'sparkle': import_folder('1 - level/graphics/particles/sparkle'),
            'leaf_attack': import_folder('1 - level/graphics/particles/leaf_attack'),
            'thunder': import_folder('1 - level/graphics/particles/thunder'),
 
            # monster deaths
            'squid': import_folder('1 - level/graphics/particles/smoke_orange'),
            'raccoon': import_folder('1 - level/graphics/particles/raccoon'),
            'spirit': import_folder('1 - level/graphics/particles/nova'),
            'bamboo': import_folder('1 - level/graphics/particles/bamboo'),
            
            # leafs 
            'leaf': (
                import_folder('1 - level/graphics/particles/leaf1'),
                import_folder('1 - level/graphics/particles/leaf2'),
                import_folder('1 - level/graphics/particles/leaf3'),
                import_folder('1 - level/graphics/particles/leaf4'),
                import_folder('1 - level/graphics/particles/leaf5'),
                import_folder('1 - levelgraphics/particles/leaf6'),
                self.reflect_images(import_folder('1 - level/graphics/particles/leaf1')),
                self.reflect_images(import_folder('1 - level/graphics/particles/leaf2')),
                self.reflect_images(import_folder('1 - level/graphics/particles/leaf3')),
                self.reflect_images(import_folder('1 - level/graphics/particles/leaf4')),
                self.reflect_images(import_folder('1 - level/graphics/particles/leaf5')),
                self.reflect_images(import_folder('1 - level/graphics/particles/leaf6'))
                )
            }

    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame,True,False)
            new_frames.append(flipped_frame)
        return new_frames

    def create_grass_particles(self,pos, groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos,animation_frames,groups)

    def create_particles(self,animation_type, pos, groups):
       # animation_frames = self.frames[animation_type]  
       # ParticleEffect(pos,animation_frames,groups)
        try:
            animation_frames = self.frames[animation_type]
            if animation_frames:  # Ensure it's not empty
                ParticleEffect(pos, animation_frames, groups)
            else:
                print(f"Warning: animation_frames for '{animation_type}' is empty.")
        except IndexError as e:
            print(f"IndexError: {e}. Retrying to create particles for '{animation_type}'")
            self.create_particles(animation_type, pos, groups)
        except KeyError as e:
            print(f"KeyError: {e}. Animation type '{animation_type}' not found in frames.")


class ParticleEffect(pygame.sprite.Sprite):
    def __init__ (self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'magic'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index +=self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()
