# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019-04-01.

from __future__ import print_function

import os
import time
from datetime import timedelta

import tensorflow as tf

from preprocess128 import preprocess
from cnews_loader_withoutSeqLens import batch_iter

from lstm_model import TRNNConfig, TextRNN

source_path = '../source/zj2ss'
trainpath = source_path + '/train-ws.txt'
validatepath = source_path + '/validate-ws.txt'

test_path = '../source/zj2ss'
testpath_name = test_path + '/test-name.txt'
testpath = test_path + '/test-noname.txt'
modelpath = '../source/zj2ss/2014model_size128.model'

model_save = '../result/model_files/zj2ss'
save_dir = model_save + '/HNS_checkpoints/128-465-ws-50-70'
save_path = os.path.join(save_dir, 'best_validation_lstm')  # 最佳验证结果保存路径
tensorboard_dir = model_save + '/HNS_tensorboard/128-465-ws-50-70'

p = preprocess(modelpath)
p.load_models()
p.setinputdatapath(trainpath)
p.settestdatapath(testpath)
p.setvalidatedatapath(validatepath)


def get_time_dif(start_time):
    """获取已使用时间"""
    end_time = time.time()
    time_dif = end_time - start_time
    return timedelta(seconds=int(round(time_dif)))


def feed_data(x1_batch, x2_batch, y_batch, keep_prob):
    feed_dict = {
        model.input_x_1: x1_batch,
        model.input_x_2: x2_batch,
        model.input_y: y_batch,
        model.keep_prob: keep_prob,
    }
    return feed_dict


def evaluate(sess, x1_, x2_, y_):
    """评估在某一数据上的准确率和损失"""
    data_len = len(x1_)
    batch_eval = batch_iter(x1_, x2_, y_, 128)
    total_loss = 0.0
    total_acc = 0.0
    for x1_batch, x2_batch, y_batch in batch_eval:
        batch_len = len(x1_batch)
        feed_dict = feed_data(x1_batch, x2_batch, y_batch, 1.0)
        loss, acc = sess.run([model.loss, model.acc], feed_dict=feed_dict)
        total_loss += loss * batch_len
        total_acc += acc * batch_len

    return total_loss / data_len, total_acc / data_len


def train():
    print("Configuring TensorBoard and Saver...")
    # 配置 Tensorboard，重新训练时，请将tensorboard文件夹删除，不然图会覆盖

    if not os.path.exists(tensorboard_dir):
        os.makedirs(tensorboard_dir)

    # 结果可视化与存储
    tf.summary.scalar("loss", model.loss)  # 可视化loss
    tf.summary.scalar("accuracy", model.acc)  # 可视化acc
    merged_summary = tf.summary.merge_all()  # 将所有操作合并输出
    writer = tf.summary.FileWriter(tensorboard_dir)  # 将summary data写入磁盘

    # 配置 Saver
    saver = tf.train.Saver()
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    print("Loading training and validation data...")
    # 载入训练集与验证集
    start_time = time.time()
    train_1, train_2, train_output = p.setinputdata(model.config.seq_length_1,
                                                    model.config.seq_length_2, flag=0)

    # print(train_3)
    val_1, val_2, val_output = p.setinputdata(model.config.seq_length_1,
                                              model.config.seq_length_2, flag=1)

    time_dif = get_time_dif(start_time)
    print("Time usage:", time_dif)

    # 创建session
    session = tf.Session()
    session.run(tf.global_variables_initializer())
    writer.add_graph(session.graph)

    print('Training and evaluating...')
    start_time = time.time()
    total_batch = 0  # 总批次
    best_acc_val = 0.0  # 最佳验证集准确率
    last_improved = 0  # 记录上一次提升批次
    require_improvement = 1000  # 如果超过1000轮未提升，提前结束训练

    flag = False
    for epoch in range(config.num_epochs):
        print('Epoch:', epoch + 1)
        batch_train = batch_iter(train_1, train_2, train_output, config.batch_size)
        for x1_batch, x2_batch, y_batch in batch_train:

            feed_dict = feed_data(x1_batch, x2_batch, y_batch, config.dropout_keep_prob)

            if total_batch % config.save_per_batch == 0:
                # 每多少轮次将训练结果写入tensorboard scalar
                s = session.run(merged_summary, feed_dict=feed_dict)
                writer.add_summary(s, total_batch)

            if total_batch % config.print_per_batch == 0:
                # 每多少轮次输出在训练集和验证集上的性能
                feed_dict[model.keep_prob] = 1.0
                loss_train, acc_train = session.run([model.loss, model.acc], feed_dict=feed_dict)
                loss_val, acc_val = evaluate(session, val_1, val_2, val_output)  # 验证当前会话中的模型的loss和acc

                if acc_val > best_acc_val:
                    # 保存最好结果
                    best_acc_val = acc_val
                    last_improved = total_batch
                    print('---在这里做了修改---保存所有提升的---')
                    saver.save(sess=session, save_path=save_path + "_" + str(total_batch))
                    improved_str = '*'
                else:
                    improved_str = ''

                time_dif = get_time_dif(start_time)
                msg = 'Iter: {0:>6}, Train Loss: {1:>6.2}, Train Acc: {2:>7.2%},' \
                      + ' Val Loss: {3:>6.2}, Val Acc: {4:>7.2%}, Time: {5} {6}'
                fmsg = msg.format(total_batch, loss_train, acc_train, loss_val, acc_val, time_dif, improved_str)
                print(fmsg)
                # 害怕控制台的信息看不到，再保存到log文件里
                filename = '../result/printLog_lstm.txt'
                with open(filename, 'a+') as f:
                    f.write(fmsg + '\n')
                # 害怕控制台的信息看不到，再保存到log文件里

            session.run(model.optim, feed_dict=feed_dict)  # 运行优化
            total_batch += 1

            if total_batch - last_improved > require_improvement:
                # 验证集正确率长期不提升，提前结束训练
                print("No optimization for a long time, auto-stopping...")
                flag = True
                break  # 跳出循环
        if flag:  # 同上
            break


config = TRNNConfig()
model = TextRNN(config)

train()
