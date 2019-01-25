# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019-01-25.

# 引入 TensorFlow
import tensorflow as tf

# 创建两个常量 Tensor
const1 = tf.constant([[2, 2]])
const2 = tf.constant([[4],
                      [4]])

# 张量相乘（multiply 是 相乘 的意思）
multiply = tf.matmul(const1, const2)

# 尝试用 print 输出 multiply 的值
print("sess.run() 之前，尝试输出 multiply 的值: {}".format(multiply))

# 创建了 Session（会话）对象
sess = tf.Session()

# 用 Session 的 run 方法来实际运行 multiply 这个
# 矩阵乘法操作，并把操作执行的结果赋值给 result
result = sess.run(multiply)
# 用 print 打印矩阵乘法的结果
print("sess.run() 之后，输出 multiply 的值: {}".format(result))

if const1.graph is tf.get_default_graph():
    print("const1 所在的图（Graph）是当前上下文默认的图")

# 关闭已用完的 Session（会话）
sess.close()

# 第二种方法来创建和关闭 Session
# 用了 Python 的上下文管理器（with ... as ... :）
with tf.Session() as sess:
    result2 = sess.run(multiply)
    print("multiply 的结果是 {} ".format(result2))
