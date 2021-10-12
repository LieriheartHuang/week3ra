### 
### Author: wenjunhuang
### Class: CSc 110
### Description: in program
###




from graphics import graphics
from random import randint

window_w, window_h = 700, 500
num_of_clouds = 4
fps = 40
ratio = 1


def drawTriangle(gui: graphics, x, y):
    global window_w, window_h, ratio
    x1 = x
    y1 = window_h // 3 * 2
    x2 = int(x + window_w * ratio)
    y2 = y1
    x3 = window_w // 2
    y3 = y
    gui.triangle(x1, y1, x2, y2, x3, y3, "brown")


def drawTree(gui, x):
    global window_h, window_w, ratio
    rect_w = int(window_w * ratio / 10)
    rect_h = int(window_h * ratio / 2)
    rect_x = x - rect_w // 2
    rect_y = int(window_h / 3 * 2)
    gui.rectangle(rect_x, rect_y, rect_w, rect_h, "brown")

    el_w = int(window_w * ratio / 6)
    el_h = int(window_h * ratio / 2)
    el_x = x
    el_y = int(window_h / 3 * 2 - el_h / 3)
    gui.ellipse(el_x, el_y, el_w, el_h, "darkgreen")


def drawPond(gui: graphics, x, y):
    global window_w, window_h, ratio
    ratio = gui.mouse_y / window_w
    el_x = x
    el_y = y
    el_w = int(window_w * ratio)
    el_h = int(window_h / 10 * ratio)
    gui.ellipse(el_x, el_y, el_w, el_h, "blue")


def drawGrass(gui: graphics):
    global window_w, window_h, ratio
    i = 0
    while i < window_w:
        gui.line(int(i), int(window_h / 3 * 2 - window_h / 10 * ratio), int(i),
                 int(window_h / 3 * 2), "forest green")
        i += window_w / 20 * ratio + 2


def main():
    global window_w, window_h, num_of_clouds, ratio, fps
    # canvas
    gui = graphics(window_w, window_h, "vanishing point")

    clouds = []
    for i in range(num_of_clouds):
        cloud_x = randint(0, window_w)
        cloud_y = randint(0, window_h // 3)
        cloud_w = randint(70, 150)
        cloud_h = randint(20, 60)
        clouds.append((cloud_x + randint(-20, 20), cloud_y + randint(-20, 20),
                       cloud_w, cloud_h))
        clouds.append((cloud_x + randint(-20, 20), cloud_y + randint(-20, 20),
                       cloud_w, cloud_h))

    # draw objects
    while True:
        gui.clear()

        # draw static
        gui.rectangle(0, 0, window_w, window_h, "cyan")
        gui.rectangle(0, window_h * 2 // 3, window_w, window_h, "lightgreen")

        gui.ellipse(window_h // 5 * 4, window_w // 5, 30, 30, "yellow")
        for cloud in clouds:
            gui.ellipse(*cloud, "white")
        gui.text(0, 0, f"X: {gui.mouse_x}\nY: {gui.mouse_y}\n", "black")

        # draw motion
        ratio = gui.mouse_y / window_h
        drawTriangle(gui, int((1 - ratio) / 2 * window_w),
                     int((1 - ratio) / 3 * 2 * window_h))
        drawGrass(gui)
        drawPond(gui, int(1 / 2 * window_w), int(
            (ratio / 5 + 2 / 3) * window_h))
        drawTree(gui, int((1 / 2 + ratio / 2) * window_w))
        drawTree(gui, int((1 / 2 - ratio / 2) * window_w))
        gui.update_frame(fps)


main()
