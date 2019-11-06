#数据以文书为单位进行加载，以文书为单位进行预测，预测一次输出准确度、召回率、然后再将所有文书的准确率、召回率求平均后，再求F值
import numpy as np

def evaluatews(y_pre_cls,y_test_cls,testdatapath):
    precision = []
    recall = []
    # 加载数据
    with open(testdatapath, 'r', encoding='utf-8') as f:
        content = f.read().split('.xls')
        base = 0
        for i in range(1, len(content)):
            pp,pt,t = 0,0,0
            item = content[i]
            allsample = item.split('\n')[1:]  # 摈弃第一个
            for y,y_,sample in zip(y_test_cls[base:base+len(allsample)],y_pre_cls[base:base+len(allsample)],allsample):
                if y_ == 1:
                    pp += 1
                    if y == 1:
                        pt += 1
                if y == 1:
                    t += 1
            if pp == 0 or t == 0:
                continue
            precision_i = pt/pp
            recall_i = pt/t
            precision.append(precision_i)
            recall.append(recall_i)
            base += len(allsample)

    print(len(precision), len(recall))

    precision_average = np.mean(np.array(precision))
    recall_average = np.mean(np.array(recall))
    f = precision_average * recall_average * 2 / (precision_average + recall_average)
    print(precision_average, recall_average, f)

















