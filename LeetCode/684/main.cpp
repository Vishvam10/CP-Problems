class Solution {
public:
  bool pathExists(vector<vector<int>> &adj, int start, int end) {

    vector<bool> vis(adj.size(), false);
    queue<int> q;

    q.push(start);
    vis[start] = true;

    while (!q.empty()) {

      int node = q.front();

      if (node == end) {
        return true;
      }

      q.pop();

      for (int i = 0; i < adj[node].size(); i++) {
        if (!vis[adj[node][i]]) {
          vis[adj[node][i]] = true;
          q.push(adj[node][i]);
        }
      }
    }

    return false;
  }

  vector<int> findRedundantConnection(vector<vector<int>> &edges) {

    vector<vector<int>> adj(edges.size() + 1);

    for (int i = 0; i < edges.size(); i++) {

      int v1 = edges[i][0];
      int v2 = edges[i][1];

      if (pathExists(adj, v1, v2)) {
        return edges[i];
      }

      adj[v1].push_back(v2);
      adj[v2].push_back(v1);
    }

    return {};
  }
};