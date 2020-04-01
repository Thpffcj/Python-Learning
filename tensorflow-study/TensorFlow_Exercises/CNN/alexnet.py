# -*- coding: UTF-8 -*-
# Created by thpffcj on 2020/3/29.
# mf1932063 何林洋

# AlexNet的trick主要包括：
# 1 成功使用RELU作为CNN的激活函数，并验证其效果在较深的网络中的效果超过了sigmoid，解决了sigmoid在深层的网络中的梯度弥散的问题。
# 2 使用Dropout来随机使得一部分神经元失活，来避免模型的过拟合，在AlexNet中，dropout主要应用在全连接层。
# 3 使用重叠的最大池化，以前在卷积神经网络中大部分都采用平均池化，在AlexNet中都是使用最大池化，最大池化可以避免平均池化的模糊化效果。
# 重叠的最大池化是指卷积核的尺寸要大于步长，这样池化层的输出之间会有重叠和覆盖，提升特征的丰富性。在AlexNet中使用的卷积核大小为3×3，
# 横向和纵向的步长都为2。
# 4 使用LRN层，对局部神经元的活动创建有竞争机制，让响应较大的值变得相对更大，并抑制反馈较小的神经元，来增强模型的泛化能力。
# 5 使用了CUDA来加速深度神经网络的训练。
# 6 数据增强，随机从256×256的原始图像中截取224×224的图像以及随机翻转。如果没有数据增强，在参数众多的情况下，卷积神经网络会陷入到过拟合中，
# 使用数据增强可以减缓过拟合，提升泛化能力。进行预测的时候，提取图片的四个角加中间位置，并进行左右翻转，一共10张图片，对它们进行预测并取10次
# 结果的平均值。在AlexNet论文中也提到了，对图像的RGB数据进行PCA处理，并做一个标准差为0.1的高斯扰动，增加一些噪声，可以降低1%的错误率。

import tensorflow as tf
import numpy as np


class AlexNet(object):
    def __init__(self, x, keep_prob, skip_layer, weights_path='DEFAULT'):
        self.x = x
        self.keep_prob = keep_prob
        self.skip_layer = skip_layer
        if weights_path == 'DEFAULT':
            self.weights_path = 'bvlc_alexnet.npy'
        else:
            self.weights_path = weights_path

        self.build_AlexNet()

    def build_AlexNet(self):
        # 第一层卷积层，卷积核的尺度为11x11，深度96，步长为4.
        conv1 = conv_layer(self.x, 96, 11, 11, 4, 4, 'conv1', groups=1, padding='VALID')
        # LRN层
        norm1 = lrn_layer(conv1, 2, 1e-4, 0.75, 'norm1')
        # 最大池化层，尺寸为3x3, 步长为2
        pool1 = max_pool_layer(norm1, 3, 3, 2, 2, 'pool1')

        # 接着是一个5x5的卷积核，深度256，步长1
        conv2 = conv_layer(pool1, 256, 5, 5, 1, 1, 'conv2', groups=2)
        # LRN层
        norm2 = lrn_layer(conv2, 2, 1e-4, 0.75, 'norm2')
        # 最大池化层，尺寸为3x3，步长为2
        pool2 = max_pool_layer(norm2, 3, 3, 2, 2, 'pool2', padding='VALID')

        # 卷积层，卷积核的尺度为3x3，深度384，步长为1.
        conv3 = conv_layer(pool2, 384, 3, 3, 1, 1, 'conv3')

        # 卷积层，卷积核的尺度为3x3，深度384，步长为1.
        conv4 = conv_layer(conv3, 384, 3, 3, 1, 1, 'conv4', groups=2)

        # 卷积层，卷积核的尺度为3x3，深度256，步长为1.
        conv5 = conv_layer(conv4, 256, 3, 3, 1, 1, 'conv5', groups=2)
        # 最大池化层，尺寸为3x3, 步长为2
        pool5 = max_pool_layer(conv5, 3, 3, 2, 2, 'pool5', 'VALID')
        pool5_flatted = tf.reshape(pool5, [-1, 6 * 6 * 256], 'pool5_flatted')

        # 全连接层，尺寸4096
        fc6 = fc_layer(pool5_flatted, 6 * 6 * 256, 4096, name='fc6')
        dropout6 = dropout(fc6, self.keep_prob)

        # 全连接层，尺寸4096
        fc7 = fc_layer(dropout6, 4096, 4096, name='fc7')
        dropout7 = dropout(fc7, self.keep_prob)

        # 输出层，1000（分类个数）
        self.fc8 = fc_output_layer(dropout7, 4096, 1000, name='fc8')

    def load_initial_weights(self, sess):
        # 将权重加载到内存中
        weights_dict = np.load(self.weights_path, encoding='bytes').item()
        for name in weights_dict:
            if name not in self.skip_layer:
                with tf.variable_scope(name, reuse=True):
                    # 将权重/偏差分配给其对应的tf变量
                    for p in weights_dict[name]:
                        # 偏差
                        if len(p.shape) == 1:
                            var = tf.get_variable('b', trainable=False)
                            sess.run(var.assign(p))
                        # 权重
                        else:
                            var = tf.get_variable('w', trainable=False)
                            sess.run(var.assign(p))


# 创建卷积层
def conv_layer(x, filter_num, filter_height, filter_width, stride_x, stride_y, name, groups=1, padding='SAME'):
    # 获取输入通道数
    channel = int(x.shape[-1])
    # 为卷积创建lambda函数
    conv2d = lambda a, b: tf.nn.conv2d(input=a, filter=b,
                                       strides=[1, stride_y, stride_x, 1], padding=padding)
    with tf.variable_scope(name) as scope:
        # 创建权重和偏差变量
        w = weights([filter_height, filter_width, int(channel / groups), filter_num])
        b = bias([filter_num])

        # 分割输入和权重并将其分别卷积
        x_split = tf.split(value=x, num_or_size_splits=groups, axis=3)
        w_split = tf.split(value=w, num_or_size_splits=groups, axis=3)
        conv_split = [conv2d(m, n) for m, n in zip(x_split, w_split)]

        # 将卷积输出合并在一起
        conv_merge = tf.concat(conv_split, axis=3)

        # 使用relu作为激活函数
        return tf.nn.relu(conv_merge + b, name='scope.name')


# 创建lrn层
def lrn_layer(x, R, alpha, beta, name, bias=1.0):
    return tf.nn.local_response_normalization(x, depth_radius=R, alpha=alpha, beta=beta, name=name, bias=bias)


# 创建最大池化层
def max_pool_layer(x, filter_height, filter_width, stride_x, stride_y, name, padding='SAME'):
    return tf.nn.max_pool(x,
                          ksize=[1, filter_height, filter_width, 1],
                          strides=[1, stride_y, stride_x, 1],
                          padding=padding, name=name)


# dropout是指在深度学习网络的训练过程中，对于神经网络单元，按照一定的概率将其暂时从网络中丢弃
# 可以解决过拟合问题
def dropout(x, keep_prob, name=None):
    return tf.nn.dropout(x, keep_prob, name)


# 创建全连接层
def fc_layer(x, input_num, output_num, name):
    with tf.variable_scope(name) as scope:
        # 创建权重和偏差变量
        w = weights([input_num, output_num])
        b = bias([output_num])
        # 使用relu作为激活函数
        return tf.nn.relu(tf.matmul(x, w) + b)


# 创建输出层
def fc_output_layer(x, input_num, output_num, name):
    with tf.variable_scope(name) as scope:
        # 创建权重和偏差变量
        w = weights([input_num, output_num])
        b = bias([output_num])
        # 使用softmax作为激活函数
        return tf.nn.softmax(tf.matmul(x, w) + b)


def weights(shape):
    return tf.get_variable('w', shape, trainable=True)


def bias(shape):
    return tf.get_variable('b', shape, trainable=True)
