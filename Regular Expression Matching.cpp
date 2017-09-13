/*
 想法：由于是正则表达式，可以考虑贪心？毕竟他自己都有一个叫做贪心的模式。。。反过来说，也就是平时的算法并不算是贪心？那么也就是说，对字符串的处理思想。。。
 现在已知的对字符串的处理思想有：

  * 直接模拟（也就是直接搜索）
  * 利用数组查找的方式，也就是分化搜索。

 当前的题目本身是一个【匹配】的题目，也就是说【存在顺序的要求】，那应该是可以采取直接搜索的方式

  遇到挫折:

   * ".*" .代表匹配任意，所以这个写法就是【任意字符出现任意多次】
   * "aa*a" 也就是说，aa-aaaaa...均可匹配

 原先的思想是，遍历pattern，增加限定规则，从而确定当前的字符串是否符合这个pattern。

 看到一个最优的答案是使用DP。
 这里思考一下带来问题的符号 -- "*"
 这个符合的意思是【当前表达式出现了0-n次】，但是关键是，我们很多时候需要考虑*之后的情况

  * c*a 与 c*c -- 对这两种处理里就很尴尬，如果我们直接强行处理的话（也就是说，检查当前字符串是否为c，是的话继续匹配，否则不进行匹配）

 解决的办法，就是利用深度优先搜索，进行分情况讨论。这里对深度优先搜索的利用点是，【可以对当前状态进行保存，从而分析不同状态下的情况】

 此题使用深度搜索的特征 -- *讨论的下一步情况依赖于之前的情况，且分支比较多
*/
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
    	// if p is empty, to sure s is empty,if so too, it's mean that we got target
        if (p.empty())    return s.empty();
        
        if ('*' == p[1])
            // x* matches empty string or at least one character: x* -> xx*
            return isMatch(s, p.substr(2)) || (!s.empty() && (s[0] == p[0] || p[0] == '.') && isMatch(s.substr(1), p));
        else
        	// else , we just consider if the string i '.'
        	return !s.empty() && (s[0] == p[0] || p[0] == '.') && isMatch(s.substr(1), p.substr(1)) 
            
    }
};

int main(){

}
