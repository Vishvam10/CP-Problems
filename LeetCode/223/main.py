class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        aw, ah = abs(ax2 - ax1), abs(ay2 - ay1)
        bw, bh = abs(bx2 - bx1), abs(by2 - by1)

        a_area, b_area = aw * ah, bw * bh

        cx1, cx2 = max(ax1, bx1), min(ax2, bx2)
        cy1, cy2 = max(ay1, by1), min(ay2, by2)

        cw, ch = cx2 - cx1, cy2 - cy1

        c_area = cw * ch if cw > 0 and ch > 0 else 0

        return a_area + b_area - c_area
