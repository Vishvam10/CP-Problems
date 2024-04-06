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
  vector<int> res;

  void traverse(Node *node) {
    if (node == nullptr) {
      return;
    }

    // traverse(node->left);
    // traverse(node->right);
    for (int i = 0; i < (node->children).size(); i++) {
      traverse((node->children)[i]);
    }

    res.emplace_back(node->val);
  }

  vector<int> postorder(Node *root) {

    traverse(root);
    return res;
    // postorder := left, right, node
  }
};