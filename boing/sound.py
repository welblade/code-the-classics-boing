import random


class SoundPlayer:
    def __init__(self, sounds):
        self.sounds = sounds

    def hit(self, speed):
        self.play_sound("hit", 5)
        if speed <= 10:
            self.play_sound("hit_slow", 1)
        elif speed <= 12:
            self.play_sound("hit_medium", 1)
        elif speed <= 16:
            self.play_sound("hit_fast", 1)
        else:
            self.play_sound("hit_veryfast", 1)

    def up(self):
        self.sounds.up.play()

    def down(self):
        self.sounds.down.play()

    def score_goal(self):
        self.play_sound("score_goal", 1)

    def bounce(self):
        self.play_sound("bounce", 5)
        self.play_sound("bounce_synth", 1)

    def play_sound(self, name, count=1):
        try:
            getattr(self.sounds, name + str(random.randint(0, count - 1))).play()
        except:
            pass
