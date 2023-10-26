bool isValidColor(vector<vector<int>> mat, vector<int> colors, int vertex, int color) {
    int n = mat.size();
    for(int i=0; i<n; i++) {
        if(mat[vertex][i] == 1 && colors[i] == color) {
            return false;
        }
    }
    return true;

}

bool solve(vector<vector<int>> mat, vector<int> colors, int vertex, int m) {

    if(vertex == mat.size()) {
        return true;
    }

    for(int color=0; color<m; color++) {

        // Set the state
        colors[vertex] = color;

        bool check = isValidColor(mat, colors, vertex, color);

        if(check) {
            // Goto next state
            bool ns = solve(mat, colors, vertex+1, m);
            if(ns) {
                return true;
            }
        }

        // Reset the state
        colors[vertex] = -1;
    }

    return false;

}

string graphColoring(vector<vector<int>> &mat, int m) {
    
    vector<int> colors(mat.size(), -1);
    bool ans = solve(mat, colors, 0, m);

    if(ans) {
        return "YES";
    }

    return "NO";


}