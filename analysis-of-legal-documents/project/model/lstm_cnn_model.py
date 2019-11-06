# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019-04-01.

import tensorflow as tf


class TRNNConfig(object):
    """RNN配置参数"""

    # 模型参数
    embedding_dim = 128  # 词向量维度
    seq_length_1 = 30  # 序列长度
    seq_length_2 = 80  # 序列长度
    num_classes = 2  # 类别数

    num_layers = 2  # 隐藏层层数
    hidden_dim = 128  # 隐藏层神经元
    rnn = 'lstm'  # lstm 或 gru
    num_filters = 256  # 卷积核数目
    kernel_size = 5  # 卷积核尺寸

    dropout_keep_prob = 0.8  # dropout保留比例
    learning_rate = 1e-3  # 学习率

    batch_size = 128  # 每批训练大小
    num_epochs = 200  # 总迭代轮次

    print_per_batch = 10  # 每多少轮输出一次结果
    save_per_batch = 10  # 每多少轮存入tensorboard


class TextRNN(object):
    """文本分类，RNN模型"""

    def __init__(self, config):
        self.config = config

        # 三个待输入的数据
        self.input_x_1 = tf.placeholder(tf.float32, [None, self.config.seq_length_1, self.config.embedding_dim],
                                        name='input_x_1')
        self.input_x_2 = tf.placeholder(tf.float32, [None, self.config.seq_length_2, self.config.embedding_dim],
                                        name='input_x_2')
        self.input_y = tf.placeholder(tf.int32, [None, self.config.num_classes], name='input_y')
        self.keep_prob = tf.placeholder(tf.float32, name='keep_prob')

        self.rnn()

    def rnn(self):
        """rnn模型"""

        def lstm_cell():  # lstm核
            return tf.contrib.rnn.BasicLSTMCell(self.config.hidden_dim, state_is_tuple=True)

        def gru_cell():  # gru核
            return tf.contrib.rnn.GRUCell(self.config.hidden_dim)

        def dropout():  # 为每一个rnn核后面加一个dropout层
            if (self.config.rnn == 'lstm'):
                cell = lstm_cell()
            else:
                cell = gru_cell()
            return tf.contrib.rnn.DropoutWrapper(cell, output_keep_prob=self.keep_prob)

        with tf.name_scope("rnn1"):
            # 多层rnn网络
            with tf.variable_scope("rnn1v"):
                cells_1 = [dropout() for _ in range(self.config.num_layers)]
                rnn_cell_1 = tf.contrib.rnn.MultiRNNCell(cells_1, state_is_tuple=True)
                _outputs_1, state_1 = tf.nn.dynamic_rnn(cell=rnn_cell_1, inputs=self.input_x_1, dtype=tf.float32,
                                                        time_major=False)  # time_major等于 false代表输入和输出的格式是[batch_size, max_time, depth]

        with tf.name_scope("rnn2"):
            # 多层rnn网络
            with tf.variable_scope("rnn2v"):
                cells_2 = [dropout() for _ in range(self.config.num_layers)]
                rnn_cell_2 = tf.contrib.rnn.MultiRNNCell(cells_2, state_is_tuple=True)
                _outputs_2, state_2 = tf.nn.dynamic_rnn(cell=rnn_cell_2, inputs=self.input_x_2, dtype=tf.float32,
                                                        time_major=False)  # time_major等于 false代表输入和输出的格式是[batch_size, max_time, depth]

        with tf.name_scope("cnn3"):
            # CNN layer
            with tf.variable_scope("cnn-var1"):
                conv3 = tf.layers.conv1d(self.input_x_1, self.config.num_filters, self.config.kernel_size,
                                         name='conv3')  # (?,26,256)
                gmp3 = tf.reduce_max(conv3, reduction_indices=[1], name='gmp3')  # (?,256)

        with tf.name_scope("cnn4"):
            # CNN layer
            with tf.variable_scope("cnn-var2"):
                conv4 = tf.layers.conv1d(self.input_x_2, self.config.num_filters, self.config.kernel_size,
                                         name='conv4')  # (?,46,256)
                gmp4 = tf.reduce_max(conv4, reduction_indices=[1], name='gmp4')  # (?,256)

        with tf.name_scope("concat"):
            concat = tf.concat([_outputs_1[:, :, -1], _outputs_2[:, :, -1], gmp3, gmp4], 1)

        with tf.name_scope("score"):
            # 全连接层，后面接dropout以及relu激活
            fc = tf.layers.dense(concat, self.config.hidden_dim,
                                 name='fc1')  # w*input+b,其中可以在此方法中指定w,b的初始值，或者通过tf.get_varable指定
            fc = tf.contrib.layers.dropout(fc, self.keep_prob)  # 根据比例keep_prob输出输入数据，最终返回一个张量
            fc = tf.nn.relu(fc)  # 激活函数，此时fc的维度是hidden_dim

            # 分类器
            self.logits = tf.layers.dense(fc, self.config.num_classes,
                                          name='fc2')  # 将fc从[batch_size,hidden_dim]映射到[batch_size,num_class]输出
            self.y_pred_cls = tf.argmax(tf.nn.softmax(self.logits), 1)  # 预测类别

        with tf.name_scope("optimize"):
            # 损失函数，交叉熵
            cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=self.logits,
                                                                    labels=self.input_y)  # 对logits进行softmax操作后，做交叉墒，输出的是一个向量
            self.loss = tf.reduce_mean(cross_entropy)  # 将交叉熵向量求和，即可得到交叉熵
            # 优化器
            self.optim = tf.train.AdamOptimizer(learning_rate=self.config.learning_rate).minimize(self.loss)

        with tf.name_scope("accuracy"):
            # 准确率
            correct_pred = tf.equal(tf.argmax(self.input_y, 1),
                                    self.y_pred_cls)  # 由于input_y也是onehot编码，因此，调用tf.argmax(self.input_y)得到的是1所在的下表
            self.acc = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
