#使用turtle库绘制一个半径为200像素的圆，再绘制圆的内接等边三角形，如下图所示。提示：如果圆的半径为R，则它的内接等边三角形的边长为 R*根号3。
import turtle
turtle.circle(200)
turtle.seth(60)
turtle.fd(200*3**(1/2))
turtle.seth(180)
turtle.fd(200*3**(1/2))
turtle.seth(300)
turtle.fd(200*3**(1/2))
