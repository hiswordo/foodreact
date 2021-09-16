import pyxel

# 16色，4個音

# pyxel.init(160, 120)

# def update():
#     if pyxel.btnp(pyxel.KEY_Q):
#         pyxel.quit()

# def draw():
#     pyxel.cls(0) #背景顏色?
#     pyxel.rect(10, 10, 20, 20, 11)

# pyxel.run(update, draw)

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

# App()

# pyxel.init(120, 120)
# pyxel.cls(1)
# pyxel.circb(60, 60, 40, 7)
# pyxel.show()


pyxel.init(120, 80)

while True:
    pyxel.cls(3)
    pyxel.rectb(
    pyxel.frame_count % 160 - 40, 20, 40, 40, 7)
    pyxel.flip()