#输入一个整数n，输出n行星号组成的三角形，如下图所示.（注意：不能用对齐的方式）
#评分标准：没有输入提示扣10分，形状不对，扣20到50分
#最后一行前面有一个空格或没有空格是正确的。若多于1个则扣10分
n=eval(input("请输入行数："))
for i in range(0,n):
    print(" "*(n-i-1)+"*"*(2*i+1))
