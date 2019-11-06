# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019-04-01.

from __future__ import print_function

import os
import time
from datetime import timedelta

import numpy as np
import tensorflow as tf
from sklearn import metrics

from preprocess128 import preprocess
from cnews_loader_withoutSeqLens import batch_iter
from evaluatewithws import evaluatews

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


def test():
    print("Loading test data...")
    start_time = time.time()
    x1_test, x2_test, y_test = p.setinputdata(model.config.seq_length_1, model.config.seq_length_2, flag=2)

    session = tf.Session()
    session.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.restore(sess=session, save_path=save_path)  # 读取保存的模型

    print('Testing...')
    print('Testing...')
    loss_test, acc_test = evaluate(session, x1_test, x2_test, y_test)
    msg = 'Test Loss: {0:>6.2}, Test Acc: {1:>7.2%}'
    print(msg.format(loss_test, acc_test))

    batch_size = 128
    data_len = len(x1_test)
    num_batch = int((data_len - 1) / batch_size) + 1

    y_test_cls = np.argmax(y_test, 1)
    y_pred_cls = np.zeros(shape=len(x1_test), dtype=np.int32)  # 保存预测结果
    for i in range(num_batch):  # 逐批次处理
        start_id = i * batch_size
        end_id = min((i + 1) * batch_size, data_len)
        feed_dict = {
            model.input_x_1: x1_test[start_id:end_id],
            model.input_x_2: x2_test[start_id:end_id],
            model.keep_prob: 1.0  # 这个表示测试时不使用dropout对神经元过滤
        }
        y_pred_cls[start_id:end_id] = session.run(model.y_pred_cls, feed_dict=feed_dict)  # 将所有批次的预测结果都存放在y_pred_cls中

    print("Precision, Recall and F1-Score...")
    print(metrics.classification_report(y_test_cls, y_pred_cls, digits=3))  # 直接计算准确率，召回率和f值

    # 混淆矩阵
    print("Confusion Matrix...")
    cm = metrics.confusion_matrix(y_test_cls, y_pred_cls)
    print(cm)

    time_dif = get_time_dif(start_time)
    print("Time usage:", time_dif)
    return y_test_cls, y_pred_cls


config = TRNNConfig()
model = TextRNN(config)

y_test_cls, y_pred_cls = test()
evaluatews(y_pre_cls=y_pred_cls, y_test_cls=y_test_cls, testdatapath=testpath_name)
