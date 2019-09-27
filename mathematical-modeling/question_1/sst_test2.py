# -*- coding: UTF-8 -*-
# Created by thpffcj on 2019/9/20.

'''
    绘制不同纬度海洋平均温度图
'''

from netCDF4 import Dataset
import pandas as pd
import matplotlib.pyplot as plt
import pylab as mpl
from matplotlib.font_manager import FontProperties

def plot_para():#设置画图参数及相关配置,如透明度,中文啥啥的
    mpl.rcParams['axes.unicode_minus']=False
    #手动设置字体路径
    return FontProperties(fname='/Users/thpffcj/Desktop/数据挖掘/数学建模/STHeiti Medium.ttc')

'''
float32 sst(time, lat, lon)
    long_name: Monthly Means of Sea Surface Temperature
    units: degC
    var_desc: Sea Surface Temperature
    level_desc: Surface
    statistic: Mean
    missing_value: -9.96921e+36
    dataset: NOAA Extended Reconstructed SST V5
    parent_stat: Individual Values
    actual_range: [-1.8     42.32636]
    valid_range: [-1.8 45. ]
unlimited dimensions: time
current shape = (1985, 89, 180)
filling on, default _FillValue of 9.969209968386869e+36 used
'''

file = "sst.mnmean.nc"
fh = Dataset(file, mode="r")

lons = fh.variables["lon"][:]
'''
[  0.   2.   4.   6.   8.  10.  12.  14.  16.  18.  20.  22.  24.  26.
  28.  30.  32.  34.  36.  38.  40.  42.  44.  46.  48.  50.  52.  54.
  56.  58.  60.  62.  64.  66.  68.  70.  72.  74.  76.  78.  80.  82.
  84.  86.  88.  90.  92.  94.  96.  98. 100. 102. 104. 106. 108. 110.
 112. 114. 116. 118. 120. 122. 124. 126. 128. 130. 132. 134. 136. 138.
 140. 142. 144. 146. 148. 150. 152. 154. 156. 158. 160. 162. 164. 166.
 168. 170. 172. 174. 176. 178. 180. 182. 184. 186. 188. 190. 192. 194.
 196. 198. 200. 202. 204. 206. 208. 210. 212. 214. 216. 218. 220. 222.
 224. 226. 228. 230. 232. 234. 236. 238. 240. 242. 244. 246. 248. 250.
 252. 254. 256. 258. 260. 262. 264. 266. 268. 270. 272. 274. 276. 278.
 280. 282. 284. 286. 288. 290. 292. 294. 296. 298. 300. 302. 304. 306.
 308. 310. 312. 314. 316. 318. 320. 322. 324. 326. 328. 330. 332. 334.
 336. 338. 340. 342. 344. 346. 348. 350. 352. 354. 356. 358.]
'''
lats = fh.variables["lat"][:]
'''
[ 88.  86.  84.  82.  80.  78.  76.  74.  72.  70.  68.  66.  64.  62.
  60.  58.  56.  54.  52.  50.  48.  46.  44.  42.  40.  38.  36.  34.
  32.  30.  28.  26.  24.  22.  20.  18.  16.  14.  12.  10.   8.   6.
   4.   2.   0.  -2.  -4.  -6.  -8. -10. -12. -14. -16. -18. -20. -22.
 -24. -26. -28. -30. -32. -34. -36. -38. -40. -42. -44. -46. -48. -50.
 -52. -54. -56. -58. -60. -62. -64. -66. -68. -70. -72. -74. -76. -78.
 -80. -82. -84. -86. -88.]
'''

north_latitude_0 = 44
north_latitude_80 = 4

sst = fh.variables["sst"]

sst_0 = sst[0, :, 30]
# print(sst_0)

year = 1854
years = []
data_0 = []
data_80 = []
month = 1
month_mean_0 = 0.0
month_mean_40 = 0.0
month_mean_80 = 0.0

for i in range(0, 1985):

    # 纬度为0的月求和
    sst_0 = sst[i, north_latitude_0,]
    month_mean_0 += pd.DataFrame(sst_0).dropna().values.mean()

    # 维度为80的月求和
    sst_80 = sst[i, north_latitude_80,]
    month_mean_80 += pd.DataFrame(sst_80).dropna().values.mean()

    month += 1

    # 求年均值
    if month == 25:
        year_mean_0 = month_mean_0 / 24
        data_0.append(year_mean_0)

        year_mean_80 = month_mean_80 / 24
        data_80.append(year_mean_80)

        years.append(year)

        month_mean_0 = 0.0
        month_mean_80 = 0.0
        month = 1
        year += 2


plt.plot(years, data_0)
# plt.plot(years, data_80)
plt.ylim(26, 28.5)
plt.xlabel('时间', FontProperties=plot_para())
plt.ylabel('温度(ºC)', FontProperties=plot_para())
plt.title("赤道海洋表面温度", FontProperties=plot_para())
plt.legend()
# plt.show()

plt.savefig('/Users/thpffcj/Desktop/数据挖掘/数学建模/2019年中国研究生数学建模竞赛赛题/2019年中国研究生数学建模竞赛E题/data/赤道海洋表面温度.png')


