import pyxel
import random
import math
import time

# @link [【Python趣味教学】教大家做一个超简单超好玩的杀死病毒像素游戏_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1F7411n7om?p=4) at 2021/9/16

W, H = 150, 150  # ?? 上限多少啊
INI_NUM_VIRUSES = 10
MAX_SPEED = 1.2
MIN_RADIUS = 3
BackgroundCOLOR = 3

class Virus:
    # init(width, height, [caption], [scale], [palette], [fps], [quit_key], [fullscreen])
    def __init__(self):
        self.radius = random.uniform(3, 10)  # 3~9全部
        self.pos = [
            random.uniform(self.radius, W - self.radius),  # x
            random.uniform(self.radius, H - self.radius),  # y
        ]
        self.speed = [
            random.uniform(-MAX_SPEED, MAX_SPEED),
            random.uniform(-MAX_SPEED, MAX_SPEED),
        ]
        _colorlist = [x for x in range(16)]
        _colorlist.remove(0)
        _colorlist.remove(BackgroundCOLOR)
        self.color = random.choice(_colorlist)
        self.surrounds = round(self.radius) + 2

    def update(self):
        # 移動 = 更新位置 = 本身位置 + 移動速度
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        # 四個方向碰到邊界彈回 = 速度*-1
        if self.speed[0] < 0 and self.pos[0] < self.radius:
            self.speed[0] *= -1
        if self.speed[0] > 0 and self.pos[0] > W - self.radius:
            self.speed[0] *= -1
        if self.speed[1] < 0 and self.pos[1] < self.radius:
            self.speed[1] *= -1
        if self.speed[1] > 0 and self.pos[1] > W - self.radius:
            self.speed[1] *= -1

    def draw(self):
        pass


class Game:
    def __init__(self):
        self.background = BackgroundCOLOR
        self.viruses = [Virus() for _ in range(INI_NUM_VIRUSES)]  # 產生10次病毒
        self.hit = False
        self.start_time = time.time() # 開始時間不對
        self.game_over = False
        pyxel.init(W, H, caption="GOGO Virus Game")  # 視窗
        pyxel.mouse(True)  # 顯示滑鼠 # !需要在run之前 # ?? 為什麼呢
        pyxel.run(self.update, self.draw)
        

    def update(self):
        virus_count = len(self.viruses)
        
        # 病毒爆炸
        # ?? btnp中的p是甚麼意思呢?
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.hit = True # 點擊後，hit值轉True
            for i in range(virus_count):
                virus = self.viruses[i]
                dx = virus.pos[0] - pyxel.mouse_x
                dy = virus.pos[1] - pyxel.mouse_y
                # 如果點選位置，在virus內部的話 (dx,dy所構成距離 < 半徑)
                # 增加判定範圍 +4.5
                if dx ** 2 + dy ** 2 < virus.radius ** 2 + 4.5: 
                    # 分裂面積和 = 原始面積
                    # 所以分裂半徑 = (原始半徑**2/分裂數量)再開根號
                    # virus.surrounds*2 讓分裂數量不要這麼多
                    new_radius = (virus.radius ** 2 / virus.surrounds) ** 0.5
                    # 大小大於"最小半徑"則分裂往原本角度四散，小於則殺掉
                    if new_radius > MIN_RADIUS:
                        for j in range(virus.surrounds):
                            angle = (2 * math.pi / virus.surrounds) * j
                            new_virus = Virus()
                            new_virus.radius = new_radius
                            # 炸開的小病毒位置 = 原大病毒位置 + (大半+小半)*角度 
                            new_virus.pos[0] = virus.pos[0] + (virus.radius+new_virus.radius)* math.cos(angle)
                            new_virus.pos[1] = virus.pos[1] + (virus.radius+new_virus.radius)* math.sin(angle)
                            new_virus.speed[0] = MAX_SPEED * math.cos(angle)
                            new_virus.speed[1] = MAX_SPEED * math.sin(angle)    
                            # 將新增的小病毒合併至原先所有病毒列表
                            self.viruses.append(new_virus)
                    del self.viruses[i]
                    break
        # 病毒融合


        for virus in self.viruses:
            virus.update()

    def draw(self):
        pyxel.cls(self.background)  # 清空螢幕，繪製黑色
        # 動態時間等於draw的time.time()-已賦值開始時間
        if not self.game_over:
            pyxel.text(5,5, f"Time:{int(time.time())-int(self.start_time)}", 0)

        if not self.hit:
            pyxel.text( 30, 75, "Let's Go, Virus Come", pyxel.frame_count % 4 )  # 起點左上 (x, y, text, color)

        # 雖然狀態還是遊戲中，但病毒已清光，將狀態轉成game_over
        if not self.game_over and len(self.viruses) == 0:
            self.game_over = True
            self.total_time = time.time() - self.start_time
        
        if self.game_over:
            pyxel.text(50, 60, "YOU WIN", pyxel.frame_count % 16 )
            pyxel.text(50, 70, f"TIME: {int(self.total_time)}S", pyxel.frame_count % 16 )

        # 顯示病毒
        for virus in self.viruses:
            pyxel.circ(
                virus.pos[0], virus.pos[1], virus.radius - 1, virus.color
            )  # -1 留給外圈
            # 顯示病毒外圈
            for i in range(virus.surrounds):
                angle = (2 * math.pi / virus.surrounds) * i
                pyxel.circ(
                    virus.pos[0] + virus.radius * math.cos(angle),
                    virus.pos[1] + virus.radius * math.sin(angle),
                    1,
                    virus.color,
                )


game = Game()

# 閃爍顏色: pyxel.frame_count % 16

# %%
import random
colorlist = [x for x in range(4)]
colorlist.remove(1)
colorlist.remove(2)
print(colorlist)
newlist = [0,1,2,0,0,3]
newlist.remove(0)
# newlist.pop(1)
print(newlist)

# print(random.choice(colorlist))
# %%
