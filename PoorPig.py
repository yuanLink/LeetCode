class Solution(object):
    import math
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        t = minutesToTest // minutesToDie + 1
        if t == 1:
            return buckets - 1
        else:
            return int(math.ceil(math.log(buckets, t)))


"""
有趣的问题，重点就在于【如何有效的利用猪】。
这个题目其实非常难，要学会递推问题:
4bucket，15min，15min总长
其实只需要2头猪（类似于编码
|---|---|---|---|
|0  |1  |2  |3  |
|---|---|---|---|
|_ _|A _|_ B|A B|

）
而8bucket，15min，30min总长呢？（此时可以让猪行动两次）
答案是2，为什么呢?
我们可以简单的将上面的算法*2(假装是有了第三头猪）。这种想法就是【利用猪给桶标号
，也就是:
|----|----|----|
|时间|A   |B   |
|----|----|----|
|0   |1   |0   |
|----|----|----|
注意如果这么做，【相当于没有利用2头猪各增加了一次行动机会】这个特征，此时其实每个
猪的编号变成了:
|-----|------|
|第一次|第二次|
|-----|------|
那么上述问题就变成了
|-------------|-------------|-------------|-------------|
|第一次A是否喝 |第二次A是否喝 |第一次B是否喝 |第二次B是否喝 |
|-------------|-------------|-------------|-------------|
也就是出现了 3 * 3 = 9 种编码
应此，我们的2其实是log(8 ,3).ceil得到的答案
"""