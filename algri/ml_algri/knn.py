from numpy import * #导入numpy库
import operator #导入operator模块
#以下代码定义了一个数据集，其中包含数据与对应的分类标签信息
def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels
group,labels=createDataSet()
# print(group)
# print(labels)

def calssify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    diffMat=tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortclassCount=sorted(classCount.items(),
    key=operator.itemgetter(1),reverse=True)
    return sortclassCount[0][0]

def files2matrix(filename):
    fr=open(filename)
    arraylines=fr.readlines()
    lenoflines=len(arraylines) #返回集合长度，这里的集合一行为一个元素
    matrix=np.zeros((lenoflines,3))#创建全0矩阵，行数为lenoflines，列数为3
    labelmatrix=[] #创建空集合
    index=0
    for line in arraylines:
        line=line.strip()
        listFromline=line.split('\t')
        matrix[index,:]=listFromline[0:3]
        labelmatrix.append(int(listFromline[-1]))
        index+=1
    return matrix,labelmatrix

import matplotlib
import matplotlib.pyplot as plt
import pylab
matplotlib.rcParams['font.sans-serif'] = ['SimHei'] #使中文字符能被显示在图表中
fig=plt.figure()
ax=fig.add_subplot(111) #图表画在分成一行一列的第一个表格中
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15*np.array(datingLabels),15*np.array(datingLabels))
ax.set_xlabel('玩视频游戏所耗时间百分比')
ax.set_ylabel('每周所消费的冰淇淋公升数')
plt.show()

ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15*np.array(datingLabels),15*np.array(datingLabels))

















