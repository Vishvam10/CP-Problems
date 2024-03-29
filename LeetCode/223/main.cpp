class Solution {
public:
  int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2,
                  int by2) {

    int aw = abs(ax2 - ax1), ah = abs(ay2 - ay1);
    int bw = abs(bx2 - bx1), bh = abs(by2 - by1);

    int a_area = aw * ah, b_area = bw * bh;

    int cx1 = max(ax1, bx1), cx2 = min(ax2, bx2);
    int cy1 = max(ay1, by1), cy2 = min(ay2, by2);
    int cw = cx2 - cx1, ch = cy2 - cy1;

    int c_area = (cw > 0 && ch > 0) ? ch * cw : 0;

    return a_area + b_area - c_area;
  }
};