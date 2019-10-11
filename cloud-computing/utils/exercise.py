# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/10/11.


import sys


class Solution:
    def maximalRectangle(self, matrix):
        """
        :n行，m列
        :param matrix:
        :return:
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        h = [0] * (m + 1)
        self.ans = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    h[j] += 1
                else:
                    h[j] = 0
            self.ans = self.robot(self.ans, h)
        return self.ans

    def robot(self, maxL, h):
        stk = []
        m = len(h) - 1
        i = 0
        while i <= m:
            if len(stk) == 0 or h[stk[-1]] < h[i]:
                stk.append(i)
                i += 1
            else:
                now_idx = stk.pop()
                if len(stk) == 0:
                    maxL = max(maxL, i * h[now_idx])
                else:
                    maxL = max(maxL, (i - stk[-1] - 1) * h[now_idx])
        return maxL


if __name__ == '__main__':

    S = Solution()
    strList = []
    for line in sys.stdin:  # 当没有接受到输入结束信号就一直遍历每一行,以换行加ctrl+D结束
        if line is '\n':  # 如果是空行就停止
            break
        tempStr = line.split()  # 对字符串利用空字符进行切片
        strList.append(tempStr)
    # print(strList)
    # print(len(strList))
    # print(len(strList[0]))
    # print(strList)
    # temp =["1011","1111","1110"]
    print(S.maximalRectangle(strList))

