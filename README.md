# GeometryToolboxForManim
Geometry toolbox for manim(community)

# Install
You should first make sure that manim(community version) has installed. For those who has build up a "manim environment, run  
```
pip install manim
```

# Usage
This tool is used to add geometric operation into manim.  
Maybe this will still work for shader version, or may not. We're happy to see similar tools for manimgl.

# Description
## Point and Vector
First things first, there are two fundimental things in this tool: `Point` and `Vector`.  
**Remember! `Point` and `Vector` are the same thing.**

We can use them by calling `Point(x,y)` and `Vector(x,y)`.  
If you want to get the x or y coordinates of `Point`s ot `Vector`s, do this:  
```
c = Point(2, 1)
x = c.x # x coord
y = c.y # y ccord
```  
```
c = Vector(2, 1)
x = c.x # x coord
y = c.y # y ccord
```  
We've also define the addtion, subtraction, and other operations on `Vector`s or `Point`s, see the demo code below.  
```
>>> Point(2, 3) + Point(1, 2)
Point(3, 5)
>>> Vector(1, 2) - Vecotr(2, 4)
Vector(1, 2)
>>> Vector(2, 3) * 2
Vector(4, 6)
>>> Vector(2, 3) / 2
Vector(1, 1.5)
>>> Point(3, 2) * Point(1, 2) # dot product
7
>>> Point(3, 2) ^ Point(1, 2) # cross product
4
>>> abs(Vector(3, 4)) # the magnitude
5
```

## Line
Lines is discribe by a point on the line and a direction.

## Circle
Circles is discribe by its center and radius.

# Examples
TODO

# Contributing
Feel free to open an issue or pull a request, and add new operations to our project.  
Here are some operation you can contribute:

- Operations about tangent circles
- Fundimental geometry operation (bisect an angle, or reflect about a line/circle/point)
- Some calculus stuff
