// for pair
#include <set>
#include <utility>

class Solution {
public:
  vector<vector<int>> floodFill(vector<vector<int>> &img, int sr, int sc,
                                int color) {

    int m = img.size();
    int n = img[0].size();
    int col = img[sr][sc];
    stack<pair<int, int>> st;

    st.push({sr, sc});

    while (!st.empty()) {
      int r = st.top().first;
      int c = st.top().second;
      st.pop();

      // is essentially a visited set
      if (img[r][c] != color) {
        // left
        if (c - 1 >= 0 && img[r][c - 1] == col) {
          st.push({r, c - 1});
        }

        // right
        if (c + 1 < n && img[r][c + 1] == col) {
          st.push({r, c + 1});
        }

        // up
        if (r - 1 >= 0 && img[r - 1][c] == col) {
          st.push({r - 1, c});
        }

        // down
        if (r + 1 < m && img[r + 1][c] == col) {
          st.push({r + 1, c});
        }

        img[r][c] = color;
      }
    }

    return img;
  }
};