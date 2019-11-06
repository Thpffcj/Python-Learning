from gensim.models import word2vec
import gensim
import numpy
from project1.util import matrixop
import jieba.analyse as ana
import random


class preprocess():
    def __init__(self, modelpath):
        self.model_path = modelpath

    def load_models(self):
        self.model = gensim.models.Word2Vec.load(self.model_path)

    def setinputdatapath(self, datapath):
        self.inputdatapath = datapath

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
            miss = [[0] * 64 for _ in range(seq_length - len(data))]
            data.extend(miss)
        return numpy.array(data)

    def vector(self, v):
        try:
            return self.model[v][:64]
        except:
            return [0] * 64

    def setinputdata(self, seq1_length, seq2_length, flag):
        data_1 = []
        data_2 = []
        output = []
        num1, num2 = 0, 0

        if flag == 0:  # 生成训练数据
            datapath = self.inputdatapath
        elif flag == 1:
            datapath = self.testdatapath
        else:
            datapath = self.validatedatapath

        f = open(datapath, 'r', encoding='utf-8')
        lines = f.read().split('\n')
        for line in lines:
            if line.strip() != '':
                ftls = (line.split('|'))[0].split(' ')
                ssls = (line.split('|'))[1].split(' ')
                label = (line.split('|'))[2]
                if label.strip()[0] == '0':
                    data_1.append(self.fixedvec([self.vector(ss) for ss in ssls], seq1_length))
                    data_2.append(self.fixedvec([self.vector(ft) for ft in ftls], seq2_length))
                    output.append([1, 0])
                    num1 += 1

                elif label.strip()[0] == '1':
                    data_1.append(self.fixedvec([self.vector(ss) for ss in ssls], seq1_length))
                    data_2.append(self.fixedvec([self.vector(ft) for ft in ftls], seq2_length))
                    output.append([0, 1])
                    num2 += 1
        print(num1)
        print(num2)
        print(len(data_1))
        return numpy.array(data_1), numpy.array(data_2), numpy.array(output)

    def settestdatapath(self, datapath):
        self.testdatapath = datapath

    # 到结论库中遍历结论，使用attention
    # inputvec是[seq1,64]
    # 每个结论也表示成jl[seq3,64]
    # reduce_mean(softmax(input*jl,0) ,1)=ai
    # o = ai的求和
    #

    def setattinputdata(self, seq1_length, seq2_length, seq3_legth, flag):
        data_1 = []
        data_2 = []
        data_3 = []
        output = []
        num1, num2 = 0, 0

        if flag == 0:  # 生成训练数据
            datapath = self.inputdatapath
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
                    if len(ssls) >= 3:
                        print(str(num1 + num2))
                        vec1 = self.fixedvec([self.vector(ss) for ss in ssls], seq1_length)
                        vec2 = self.fixedvec([self.vector(ft) for ft in ftls], seq2_length)
                        # 扩展：
                        # 0、获取关键词
                        # 1、获取扩展集
                        # 2、获取扩展数据
                        keywords = ana.extract_tags(line.split('|')[1], topK=3)
                        input_bj = self.filterbj(keywords)
                        vec3 = self.attention(vec1, input_bj, seq3_legth)

                        data_1.append(vec1)
                        data_2.append(vec2)
                        data_3.append(vec3)
                        output.append([1, 0])
                    num1 += 1

                elif label.strip()[0] == '1':
                    print(str(num1 + num2))
                    vec1 = self.fixedvec([self.vector(ss) for ss in ssls], seq1_length)
                    vec2 = self.fixedvec([self.vector(ft) for ft in ftls], seq2_length)
                    # 扩展：
                    # 0、获取关键词
                    # 1、获取扩展集
                    # 2、获取扩展数据
                    keywords = ana.extract_tags(line.split('|')[1], topK=3)
                    input_bj = self.filterbj(keywords)
                    vec3 = self.attention(vec1, input_bj, seq3_legth)

                    data_1.append(vec1)
                    data_2.append(vec2)
                    data_3.append(vec3)
                    output.append([0, 1])
                    num2 += 1

        print('len(data1)', len(data_1))
        print('len(data2)', len(data_2))
        return numpy.array(data_1), numpy.array(data_2), numpy.array(data_3), numpy.array(output)

    def filterbj(self, keywords):
        input_bj = []
        for bj in self.bj:
            count = 0
            for i in keywords:
                if bj.count(i) > 0:
                    count += 1
            if count >= 2:
                input_bj.append(bj)

        # 随机选取5个
        if len(input_bj) > 5:
            indexs = random.sample(range(0, len(input_bj)), 5)
        else:
            return input_bj
        new_bj = []
        for i in indexs:
            new_bj.append(input_bj[i])
        return new_bj

    # 对补集做attention
    def attention1(self, inputvec, input_bj, seq3_legth):
        a = []
        if len(input_bj) > 0:
            for bj in input_bj:
                bjls = list(filter(lambda x: x.strip() != '', bj.split(' ')))
                di = self.fixedvec([self.vector(ss) for ss in bjls], seq3_legth)  # [seq3,d]
                simMatrix = numpy.matmul(inputvec, di.T)  # [seqone,seq3]
                aisoft = matrixop.softmaxMatrix(simMatrix)
                # print('aisoft',aisoft)
                ai = matrixop.sumMatrix(aisoft)  # [1,seq3]
                # print(ai)

                for i in range(seq3_legth):
                    di[i] = di[i] * ai[i]

                ad = di
                # ad = numpy.matmul(ai, di)  # [seq1,seq3]*[seq3,d] = [seq1,d]
                a.append(ad.tolist())
            o = (matrixop.sumMatrix(numpy.array(a))) / len(input_bj)  # [seq3,d]
        else:
            o = numpy.zeros(shape=(seq3_legth, 64))
        return o

    # 不对补集做attetion
    def attention(self, inputvec, input_bj, seq3_length):
        a = []
        if len(input_bj) > 0:
            for bj in input_bj:
                bjls = list(filter(lambda x: x.strip() != '', bj.split(' ')))
                di = self.fixedvec([self.vector(ss) for ss in bjls], seq3_length)  # [seq3,d]
                a.append(di.tolist())
            o = (matrixop.sumMatrix(numpy.array(a))) / len(input_bj)  # [seq3,d]

        else:
            o = numpy.zeros(shape=(seq3_length, 64
                                   ))
        return o
