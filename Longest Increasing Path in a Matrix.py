class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        """
        决定使用Python的思想解决问题
        添加变量：dis用于设定从x到y的距离
        """
        h = len(matrix)
        if h == 0:
            return 0
        w = len(matrix[0])
        if w == 0:
            return 0
        distance= [[0]*w for i in range(h)]
        
        """
        使用深度遍历的函数
        结果：返回所存储的，从x-y的点数
        """
        def dps(x,y):
            for i , j in zip([1,0,-1,0],[0,1,0,-1]):
                #向对应的位置前进
                nx,ny = x+i,y+j
                if 0<=nx<h and 0<=ny<w and matrix[x][y]<matrix[nx][ny]:
        #若该点还没有访问过
                    if not distance[nx][ny]:
                        distance[nx][ny] = dps(nx,ny)
                    distance[x][y] = max(distance[nx][ny]+1,distance[x][y])
        #设置边界值：每个点至少为1
            distance[x][y] = max(distance[x][y],1)
            return distance[x][y]
        """
        主函数
        """
        maxnum = 0
        for x in range(h):
            for y in range(w):
                distance[x][y] = dps(x,y)
                maxnum = max(maxnum,distance[x][y])
        return maxnum
        
        """
        算法：
        0.给每个点所在的坐标设立一个集合，若这个集合为false，则设定这个点未访问过，否则视为访问过
        1.遍历每个点
        2.遍历这个点周围的点，若比其大，则压入栈中，并且访问此点，将max值增加
        3.若四周均不可访问，则将此点弹出，进入上一个点
        4.当所有的点均访问过后，则结束循环
        
        使用深度遍历+动态规划
        动态规划思想：由于是寻找“最多的点”，可以用一个二维数组来存储“从x到y总共有多少个点”（dis[x][y] = num)
        然后由于是动态规划，正好会避开重复的结果。
        实现方法：利用深度遍历
        """
