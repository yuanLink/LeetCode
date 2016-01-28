class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        """
        解法：利用换底公式loga(b) = logc(b)/logc(a),只需要判断其是否为整数即可（判断整数的方法
        很简单：int(a) == a即可
        注意！听说不能直接使用log3(n)尝试中
        果然不行…………
        """
        if n>0:
            a = math.log10(n)/math.log10(3)
            return a == int(a)
        else:
            return False
        
