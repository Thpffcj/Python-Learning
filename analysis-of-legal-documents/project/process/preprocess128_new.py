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
        if len(data) < seq_length:
            miss = [[0] * 128 for _ in range(seq_length - len(data))]
            data.extend(miss)
            return numpy.array(data)
        else:
            return numpy.array(data[:seq_length])

    def vector(self, v):
        try:
            return self.model[v]
        except:
            return [0] * 128

    def setinputdata(self, seq1_length, seq2_length, flag):
        longest_seqlen = 0
        data_1 = []
        data_2 = []
        output = []
        num1, num2 = 0, 0

        data_1_seqlens = []
        data_2_seqlens = []

        if flag == 0:  # 生成训练数据
            datapath = self.inputdatapath
        elif flag == 1:
            datapath = self.validatedatapath
        else:
            datapath = self.testdatapath

        f = open(datapath, 'r', encoding='utf-8')
        lines = f.read().split('\n')
        #
        print('--这里是我设置的----避免memory error而减少训练数据----')
        zheng = 20000
        fu =20000
        print('--这里是我设置的----避免memory error而减少训练数据----')
        longest_seq_len = 1022
        for line in lines:
            if line.strip() != '':

                ftls = (line.split('|'))[0].split(' ')
                ssls = (line.split('|'))[1].split(' ')
                label = (line.split('|'))[2]
                if ssls[0] != '上述事实':
                    if label.strip()[0] == '0':
                        if fu == 0:
                            pass
                        else:
                            data_1.append(self.fixedvec([self.vector(ss) for ss in ssls], seq1_length))
                            data_2.append(self.fixedvec([self.vector(ft) for ft in ftls], seq2_length))
                            output.append([1, 0])
                            num1 += 1
                            fu -= 1
                            if len(ssls) <= seq1_length:
                                data_1_seqlens.append(len(ssls))
                            else:
                                data_1_seqlens.append(seq1_length)
                            if (len(ftls)) <= seq2_length:
                                data_2_seqlens.append(len(ftls))
                            else:
                                data_2_seqlens.append(seq2_length)
                    else:
                        if zheng == 0:
                            pass
                        else:
                            data_1.append(self.fixedvec([self.vector(ss) for ss in ssls], seq1_length))
                            data_2.append(self.fixedvec([self.vector(ft) for ft in ftls], seq2_length))
                            output.append([0, 1])
                            num2 += 1
                            zheng -= 1
                            if len(ssls) <= seq1_length:
                                data_1_seqlens.append(len(ssls))
                            else:
                                data_1_seqlens.append(seq1_length)
                            if (len(ftls)) <= seq2_length:
                                data_2_seqlens.append(len(ftls))
                            else:
                                data_2_seqlens.append(seq2_length)
        print(num1)
        print(num2)
        return numpy.array(data_1), numpy.array(data_2), numpy.array(output)
