from typing import *

def graphColoring(mat: List[List[int]], m: int) -> str:
    
    def isValidColor(vertex, color) :
        for i in range(n) :
            if(mat[vertex][i] == 1 and colors[i] == color) :
                return False
        return True


    def solve(vertex) :
        if(vertex == n) :
            return True

        for color in range(m) :
  
            check = isValidColor(vertex, color)
            if(check) :

                # Set the state
                colors[vertex] = color

                # Goto next state
                ns = solve(vertex + 1)
                if(ns) :
                    return True

                # Reset the state
                colors[vertex] = -1

    n = len(mat)
    colors = [-1 for i in range(n)]

    ans = solve(0)
    
    return "YES" if ans else "NO"





