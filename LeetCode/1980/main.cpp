class Solution {
public:
  string findDifferentBinaryString(vector<string> &arr) {

    /*

        1 1 0 0
        1 1 0 1
        1 1 1 0
        1 1 1 1

        see diagonals, switch to create new element

    */

    // given that arr[i].length() == n
    int n = arr.size();
    string s;

    for (int i = 0; i < n; i++) {
      if (arr[i][i] == '1') {
        s += "0";
      } else {
        s += "1";
      }
    }

    return s;
  }
};