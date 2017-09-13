#include<iostream>
#include<string>
#include<cstring>

using namespace std;

string input;
char answer[1001];
/* 
			inStr
  To share the str is a parlindromic or not
  int begin: the begin index of the str
  int end: the end of the maybe-parlindromic
  int length: the length of the substring
  char* str: string that we need to find parlindromic
*/
bool inStr(int begin, int end,int length, const char* str) {
	int len = strlen(str);
	for (int i = begin; i < length; i++) {
		if (str[end - (i - begin)] != str[i])
			return false;
	}
	return true;
}

char* find_long_parlindromic(string input_t) {
	char* p_begin, *p_split,*p_end;
	const char* input = input_t.c_str();
	int len = strlen(input);
	int max_length = 0;
	for (int i = 0; i < len - 1; i++) {
		for (int j = i + 1; j < len; j++) {
			if (inStr(i, j, (j + i + 1) / 2, input)) {
				if (max_length < j - i + 1) {
					memset(answer, 0, sizeof(answer));
					memcpy(answer, &input[i], j - i + 1);
					max_length = j - i + 1;
				}
			}
		}
	}
	string ans;
	ans[0];
	ans.append(answer);
	return answer;
}

string find_long_parlindromic_(string s) {
	if (s.empty()) return "";
	if (s.length() == 1) return s;
	int split, begin, end;
	int max_length = 1, min_begin = 0;
	for (split = 0; split < s.size();) {
		// if last string is shorter than our longest string, we just break
		if (s.size() - split <= max_length / 2) break;
		// first, we should now that to parlindromic string, same string are always is parlindromic
		// so we just add this string into our parlindromic string 
		begin = split; end = split;
		while (end < s.size() - 1 && s[end] == s[end + 1]) end++;
		// that we can know next time we should look for
		split = end + 1;
		// checkout the stirng that except duplication string, we could find others string that is parlindromic>
		while (end < s.size() - 1 && begin > 0 && s[end + 1] == s[begin - 1]) {
			begin--; end++;
		}
		// finally, we can sure that between begin and end, string are always parlindromic
		if (max_length < end - begin + 1) {
			max_length = end - begin + 1;
			min_begin = begin;
		}
	}
	return s.substr(min_begin, max_length);
}
int main() {
	
	cin >> input;
	
	// use three pointer, first point to begin of now string, second point to split point,
	// third point to the "maybe parlindromic string"
	// this is right! but I did not use this so it can not pass.....
	// Right answer is nearly same to that except that they use [split pointer] as the variable instead 
	// of now pointer
	//char* answer;
	string ans = find_long_parlindromic_(input);
	cout << ans << endl;
	return 0;
}