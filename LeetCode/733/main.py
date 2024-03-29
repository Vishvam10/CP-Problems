class Solution:
    def floodFill(self, img: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        m = len(img)
        n = len(img[0])
        col = img[sr][sc]
        st = [(sr, sc)]

        while (st):

            r, c = st[-1]
            st.pop()

            # if not visited
            if (img[r][c] != color):

                # left
                if (c - 1 >= 0 and img[r][c-1] == col):
                    st.append((r, c-1))

                # right
                if (c + 1 < n and img[r][c+1] == col):
                    st.append((r, c+1))

                # up
                if (r - 1 >= 0 and img[r-1][c] == col):
                    st.append((r-1, c))

                # down
                if (r + 1 < m and img[r+1][c] == col):
                    st.append((r+1, c))

                img[r][c] = color

        return img
