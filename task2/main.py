"""Pythagorean tree fractal using recursion"""
import turtle


def pythagorean_tree(turtle_obj, length, depth):
    """Draw Pythagorean tree fractal recursively with colors and varying line width"""
    if depth == 0:
        return

    turtle_obj.pensize(max(1, depth * 0.8))

    turtle_obj.forward(length)
    pos = turtle_obj.position()
    heading = turtle_obj.heading()

    turtle_obj.left(45)
    pythagorean_tree(turtle_obj, length * 0.7, depth - 1)

    turtle_obj.setposition(pos)
    turtle_obj.setheading(heading)

    turtle_obj.right(45)
    pythagorean_tree(turtle_obj, length * 0.7, depth - 1)

    turtle_obj.setposition(pos)
    turtle_obj.setheading(heading)


if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії: ") or "5")

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title(f"Дерево Піфагора (рівень {level})")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()

    pythagorean_tree(t, 100, level)

    screen.exitonclick()
