import gensim
import numpy


class preprocess():
    def __init__(self, modelpath):
        self.model_path = modelpath

    def load_models(self):
        self.model = gensim.models.Word2Vec.load(self.model_path)

    def setinputdatapath(self, datapath):
        self.inputdatapath = datapath

    def settestdatapath(self, datapath):
        self.testdatapath = datapath

    def setvalidatedatapath(self, datapath):
        self.validatedatapath = datapath

    def setbjpath(self, datapath):  # 补集
        self.bjpath = datapath

    def setbj(self):
        f = open(self.bjpath, 'r', encoding='utf-8')
        s = f.read().split('\n')
        f.close()
        self.bj = s

    def fixedvec(self, data, seq_length):
        if (len(data) >= seq_length):
            data = data[:seq_length]
        else:
            miss = [[0] * 128 for _ in range(seq_length - len(data))]
            data.extend(miss)
        return numpy.array(data)

    def vector(self, v):
        try:
            return self.model[v]
        except:
            return [0] * 128

    def setinputdata(self, seq1_length, seq2_length, flag):
        data_1 = []
        data_2 = []
        output = []
        num1, num2 = 0, 0
        numbers = 50000

        if flag == 0:  # 生成训练数据
            datapath = self.inputdatapath
            numbers = 25000
        elif flag == 1:
            datapath = self.validatedatapath
            numbers = 5500
        else:
            datapath = self.testdatapath

        f = open(datapath, 'r', encoding='utf-8')
        lines = f.read().split('\n')
        for line in lines:
            if line.strip() != '':

                ftls = (line.split('|'))[0].split(' ')
                ssls = (line.split('|'))[1].split(' ')
                label = (line.split('|'))[2]
                if label.strip()[0] == '0':
                    if num1 >= numbers:
                        pass
                    else:
                        # 为什么在这里先ss，保持一致顺序多好
                        data_1.append(self.fixedvec([self.vector(ss) for ss in ssls], seq1_length))
                        data_2.append(self.fixedvec([self.vector(ft) for ft in ftls], seq2_length))
                        output.append([1, 0])
                        num1 += 1
                else:
                    if num2 >= numbers:
                        pass
                    else:
                        data_1.append(self.fixedvec([self.vector(ss) for ss in ssls], seq1_length))
                        data_2.append(self.fixedvec([self.vector(ft) for ft in ftls], seq2_length))
                        output.append([0, 1])
                        num2 += 1
        print(num1)
        print(num2)
        print(len(data_1))
        return numpy.array(data_1), numpy.array(data_2), numpy.array(output)

    def data_length(self):
        zj_length = 0
        ss_length = 0
        number = 0
        short_number = 0
        zj_data_length = []
        ss_data_length = []

        data_path = self.model_path

        f = open(data_path, 'r', encoding='utf-8')
        lines = f.read().split('\n')
        for line in lines:
            if line.strip() != '':
                zjls = (line.split('|'))[0].split(' ')
                ssls = (line.split('|'))[1].split(' ')
                zj_len = 0
                ss_len = 0
                for zj in zjls:
                    zj_len = zj_len + len(zj)
                for ss in ssls:
                    ss_len = ss_len + len(ss)
                if zj_len < 80:
                    short_number = short_number + 1
                zj_length = zj_length + zj_len
                ss_length = ss_length + ss_len
                zj_data_length.append(zj_len)
                ss_data_length.append(ss_len)
                number = number + 1
        zj_length = zj_length / number
        ss_length = ss_length / number
        '''
        zj : 0 - 10 : 6071
             0 - 30 : 26939
             0 - 80 : 55085
        ss : 0 - 10 : 16068
             0 - 30 : 60797
        '''
        print(short_number)
        # zj std:107.651189996
        print('zj std:' + str(numpy.array(zj_data_length).std()))
        # ss std:17.2803096748
        print('ss std:' + str(numpy.array(ss_data_length).std()))
        # 84.1428588964586
        # 22.93348063585589
        print(zj_length)
        print(ss_length)


if __name__ == '__main__':
    model_path = '../../source/zj2ss/train-ws.txt'
    p = preprocess(model_path)
    p.data_length()
