#include <stdio.h>
#include <math.h>

long long int createPalidrome(long long int num, int n);
int largestPalindrome(int n) {
    if(n == 1)
        return 9;
    long int pedding = 1;
    long int i;
    for(i = 0; i < n; i++){
        pedding *= 10;
    }
    """
    the most important is to [bisection number], because it's palidrome,
    so it's number is half equal, we just talk aboubt half num, just O(n),
    """
    long long int upperBound = pedding - 1, lowerBound = pedding / 3;
    """
    use upperBound and lowerBound to ensure that we just need to try this
    """
    long long int maxNum = upperBound * upperBound;
    // we just need the halfNum of maxNum
    long long int halfNum = maxNum/pedding;
    bool isPalidrome = false;
    long long int palidrome = 0;
    while(!isPalidrome){
        palidrome = createPalidrome(halfNum, n);
        for(i = upperBound; i>= lowerBound; i--){
            if (i*i < palidrome)
                break;
            if (palidrome % i  == 0 && (palidrome / i)<upperBound){
                isPalidrome = true;
                return palidrome % 1337;
            }
        }
        halfNum -= 1;
    }
    return palidrome % 1337;
}
long long int createPalidrome(long long int num, int n){
    long long int ans = num;
    int lastNum[8];
    int i = 0;
    for(i = 0; num!=0; i++){
        lastNum[i] = num%10;
        num/= 10;
    }
    int j = i;
    for(i = 0; i < j; i++){
        ans*=10;
        ans+=lastNum[i];
    }
    return ans;
}