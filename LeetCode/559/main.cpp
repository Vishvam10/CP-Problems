/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
  int maxDepth(Node *node) {
    if (node == NULL) {
      return 0;
    }

    int res = 0;
    for (int i = 0; i < node->children.size(); i++) {
      int child = maxDepth(node->children[i]);
      res = max(res, child);
    }
    // int left = maxDepth(node->left);
    // int right = maxDepth(node->right);

    return 1 + res;
  }
};