import turtle
import lsystem

def main():
    t = turtle.Turtle()
    t.speed(0)
    wd = turtle.Screen()
    wd.tracer(10) #reduce this number if you want things to go slower

    print("Test # 1: The Arrowhead Curve\n######################################\n")
    sys = lsystem.LSystem("arrowheadcurve.txt")
    sys.createLSystem()
    t.up()
    t.setx((-(wd.window_width() / 2)) + 10)
    t.down()
    sys.drawLSystem(t)
    t.clear()
    t.reset()

    print("Test # 2: The Hilbert Curve\n######################################\n")
    sys2 = lsystem.LSystem("hilbertcurve.txt")
    sys2.createLSystem()
    t.up()
    t.setx((-(wd.window_width() / 2)) + 10)
    t.sety(((wd.window_height() / 2)) - 10)
    t.down()
    sys2.drawLSystem(t)
    t.clear()
    t.reset()

    print("Test # 3: The Dragon Curve\n######################################\n")
    sys3 = lsystem.LSystem("dragoncurve.txt")
    sys3.createLSystem()
    t.up()
    t.setx(0)
    t.down()
    sys3.drawLSystem(t)
    t.clear()
    t.reset()

    print("Test # 4: The Peano-Gosper Curve\n######################################\n")
    sys4 = lsystem.LSystem("peanogospercurve.txt")
    sys4.createLSystem()
    sys4.drawLSystem(t)
    t.clear()
    t.reset()

    print("Test # 5: The Sierpinski Triangle Curve\n######################################\n")
    sys5 = lsystem.LSystem("sierpinskitrianglecurve.txt")
    sys5.createLSystem()
    t.up()
    t.setx((-(wd.window_width() / 2)) + 10)
    t.sety((-(wd.window_height() / 2)) + 20)
    t.down()
    sys5.drawLSystem(t)
    t.clear()
    t.reset()

    print("Test # 6: The Tree Curve\n######################################\n")
    sys5 = lsystem.LSystem("tree.txt")
    sys5.createLSystem()
    t.up()
    t.setx(-(wd.window_width() / 2))
    t.down()
    sys5.drawLSystem(t)
    t.clear()
    t.reset()
main()
