# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019-03-30.

import tensorflow as tf


# HAN
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

        with tf.name_scope("bilstm"):
            with tf.variable_scope("bi-lstm1"):
                cell_fw = [dropout() for _ in range(self.config.num_layers)]
                cell_bw = [dropout() for _ in range(self.config.num_layers)]

                cell_fw = tf.contrib.rnn.MultiRNNCell(cell_fw, state_is_tuple=True)
                cell_bw = tf.contrib.rnn.MultiRNNCell(cell_bw, state_is_tuple=True)

                init_state_fw = cell_fw.zero_state(batch_size=self.config.batch_size, dtype=tf.float32)
                init_state_bw = cell_bw.zero_state(batch_size=self.config.batch_size, dtype=tf.float32)

                _outputs_1, state_1 = tf.nn.bidirectional_dynamic_rnn(cell_fw=cell_fw, cell_bw=cell_bw,
                                                                      inputs=self.input_x_1,
                                                                      initial_state_fw=init_state_fw,
                                                                      initial_state_bw=init_state_bw)

            with tf.variable_scope("bi-lstm2"):
                cell_fw = [dropout() for _ in range(self.config.num_layers)]
                cell_bw = [dropout() for _ in range(self.config.num_layers)]

                cell_fw = tf.contrib.rnn.MultiRNNCell(cell_fw, state_is_tuple=True)
                cell_bw = tf.contrib.rnn.MultiRNNCell(cell_bw, state_is_tuple=True)

                init_state_fw = cell_fw.zero_state(batch_size=self.config.batch_size, dtype=tf.float32)
                init_state_bw = cell_bw.zero_state(batch_size=self.config.batch_size, dtype=tf.float32)

                _outputs_2, state_2 = tf.nn.bidirectional_dynamic_rnn(cell_fw=cell_fw, cell_bw=cell_bw,
                                                                      inputs=self.input_x_2,
                                                                      initial_state_fw=init_state_fw,
                                                                      initial_state_bw=init_state_bw)

        with tf.name_scope("attention1"):
            dot1 = tf.matmul(_outputs_1[0], _outputs_2[0], adjoint_b=True)
            # 对行做attention
            beta1 = tf.nn.softmax(dot1, axis=2)
            alpha1 = tf.nn.softmax(dot1, axis=1)

        with tf.name_scope("attention2"):
            dot2 = tf.matmul(_outputs_1[1], _outputs_2[1], adjoint_b=True)
            # 对行做attention
            beta2 = tf.nn.softmax(dot2, axis=2)
            alpha2 = tf.nn.softmax(dot2, axis=1)

        with tf.name_scope('cnn1'):
            conv1 = tf.layers.conv1d(beta1, self.config.num_filters, self.config.kernel_size, name='conv1')
            gmp1 = tf.reduce_max(conv1, reduction_indices=[1], name='gmp1')

        with tf.name_scope('cnn2'):
            conv2 = tf.layers.conv1d(alpha1, self.config.num_filters, self.config.kernel_size, name='conv2')
            gmp2 = tf.reduce_max(conv2, reduction_indices=[1], name='gmp2')

        with tf.name_scope('cnn3'):
            conv3 = tf.layers.conv1d(beta2, self.config.num_filters, self.config.kernel_size, name='conv3')
            gmp3 = tf.reduce_max(conv3, reduction_indices=[1], name='gmp3')

        with tf.name_scope('cnn4'):
            conv4 = tf.layers.conv1d(alpha2, self.config.num_filters, self.config.kernel_size, name='conv4')
            gmp4 = tf.reduce_max(conv4, reduction_indices=[1], name='gmp4')

        with tf.name_scope("cnn5"):
            # CNN layer
            with tf.variable_scope("cnn-var1"):
                conv5 = tf.layers.conv1d(self.input_x_1, self.config.num_filters, self.config.kernel_size,
                                         name='conv5')  # (?,26,256)
                gmp5 = tf.reduce_max(conv5, reduction_indices=[1], name='gmp5')  # (?,256)

        with tf.name_scope("cnn6"):
            # CNN layer
            with tf.variable_scope("cnn-var2"):
                conv6 = tf.layers.conv1d(self.input_x_2, self.config.num_filters, self.config.kernel_size,
                                         name='conv6')  # (?,46,256)
                gmp6 = tf.reduce_max(conv6, reduction_indices=[1], name='gmp6')  # (?,256)

        with tf.name_scope("concat"):
            concat = tf.concat([gmp1, gmp2, gmp3, gmp4, gmp5, gmp6], 1)

        with tf.name_scope("score"):
            # 全连接层，后面接dropout以及relu激活
            # w*input+b,其中可以在此方法中指定w,b的初始值，或者通过tf.get_varable指定
            fc = tf.layers.dense(concat, self.config.hidden_dim,
                                 kernel_regularizer=tf.contrib.layers.l2_regularizer(0.01),
                                 activity_regularizer=tf.contrib.layers.l2_regularizer(0.01),
                                 name='fc1')
            fc = tf.contrib.layers.dropout(fc, self.keep_prob)  # 根据比例keep_prob输出输入数据，最终返回一个张量
            fc = tf.nn.relu(fc)  # 激活函数，此时fc的维度是hidden_dim

            # 分类器
            self.logits = tf.layers.dense(fc, self.config.num_classes,
                                          name='fc2')  # 将fc从[batch_size,hidden_dim]映射到[batch_size,num_class]输出
            self.y_pred_cls = tf.argmax(tf.nn.softmax(self.logits), 1)  # 预测类别

        with tf.name_scope("optimize"):
            # 损失函数，交叉熵
            # 对logits进行softmax操作后，做交叉墒，输出的是一个向量
            cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=self.logits, labels=self.input_y)
            regularization_losses = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)
            # 将交叉熵向量求和，即可得到交叉熵
            self.loss = tf.reduce_mean(cross_entropy) + 0.01 * sum(regularization_losses)
            # 优化器
            self.optim = tf.train.AdamOptimizer(learning_rate=self.config.learning_rate).minimize(self.loss)

        with tf.name_scope("accuracy"):
            # 准确率
            correct_pred = tf.equal(tf.argmax(self.input_y, 1),
                                    self.y_pred_cls)  # 由于input_y也是onehot编码，因此，调用tf.argmax(self.input_y)得到的是1所在的下表
            self.acc = tf.reduce_mean(tf.cast(correct_pred, tf.float32))