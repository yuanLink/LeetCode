class Solution(object):
    
    def findTheList(self,temp_list,ll,k,num,n,ak):
        """
        temp_list is the answer list
        ll is the final list save the answer list
        k is the left num(if it's 0,just return )
        num is the number can be minutes
        ak is the last number added
        n is the temptation at combinationSum3
        """
        if k == 0 and num == 0:
            return True
        elif k == 0 and num!= 0:
            return False
        
        for each in range(ak,10):
            if each > n:
                return False
            elif each <=n:
                temp_list.append(each)
                print("add " + str(each) +"it ")
                if self.findTheList(temp_list,ll,k - 1,num - each,n,each+1):
                    print("OK ! add it ")
                    ll.append([ i for i in temp_list])
                temp_list.pop()
                    
        return False
    
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        answer = []
        temp_answer = []
        for each in range(1,10):
            temp_answer.append(each)
            print("now is "+str(each))
            self.findTheList(temp_answer,answer,k - 1 ,n -each,n,each+1)
            temp_answer=[]
        return answer
    
    
