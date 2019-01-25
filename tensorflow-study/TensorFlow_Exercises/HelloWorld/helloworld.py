# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019-01-25.

# 引入 TensorFlow 库
import tensorflow as tf

# 创建一个 Constant（常量）Operation（操作）
hw = tf.constant("Hello World! I love TensorFlow!")  # 我爱 TensorFlow

# 启动一个 TensorFlow 的 Session（会话）
sess = tf.Session()

# 运行 Graph（计算图）
print(sess.run(hw))

# 关闭 Session（会话）
sess.close()