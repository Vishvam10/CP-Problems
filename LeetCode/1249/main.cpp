class Solution {
public:
    string minRemoveToMakeValid(string s) {
        
        int n = s.length();

        int ptr = 0;
        string ans;

        for(int i = 0; i < n; ++i) {
            char ch = s[i];
            if(ch == '(') {
                ptr++;
            } else if(ch == ')') {
                if(ptr <= 0) {
                    s[i] = '$';
                } else {
                    ptr--;
                }
            }
        }

        // There can still be open ones .. so handling that
        for(int i = s.length() - 1; i >= 0; --i) {
            if(ptr > 0 && s[i] == '(') {
                s[i] = '$';
                ptr--;
            }
        }
        
        for (char c : s) {
            if (c != '$') {
                ans += c;
            }
        }

        return ans;
    }
};

/*

Using stack .. unoptimized

class Solution {
public:
  string minRemoveToMakeValid(string s) {

    int n = s.length();
    string ans = "";

    // stack := (redundant bracket, index of it)
    stack<pair<char, int>> st;

    for (int i = 0; i < n; i++) {
      char ch = s[i];
      if (ch == '(') {
        st.push({ch, i});
      } else if (ch == ')') {
        if (!st.empty() && st.top().first == '(') {
          // remove the (
          st.pop();
        } else {
          // add the ) to the stack as it too is redundant
          st.push({ch, i});
        }
      }
    }

    for (int i = n - 1; i >= 0; i--) {
      if (!st.empty() && i == st.top().second) {
        st.pop();
      } else {
        ans += s[i];
      }
    }

    reverse(ans.begin(), ans.end());

    return ans;
  }
};
*/
