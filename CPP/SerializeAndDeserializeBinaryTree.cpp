#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

class Codec {
public:
  // Level-order encoding: node value, or '#' for a missing child.
  std::string serialize(TreeNode *root) {
    if (!root)
      return "";
    std::ostringstream out;
    std::queue<TreeNode *> q;
    q.push(root);
    bool first = true;
    while (!q.empty()) {
      TreeNode *node = q.front();
      q.pop();
      if (!first)
        out << ",";
      first = false;
      if (node) {
        out << node->val;
        q.push(node->left);
        q.push(node->right);
      } else {
        out << "#";
      }
    }
    return out.str();
  }

  TreeNode *deserialize(std::string data) {
    if (data.empty())
      return nullptr;
    std::vector<std::string> tokens;
    std::stringstream ss(data);
    std::string tok;
    while (std::getline(ss, tok, ','))
      tokens.push_back(tok);
    TreeNode *root = new TreeNode(std::stoi(tokens[0]));
    std::queue<TreeNode *> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty()) {
      TreeNode *node = q.front();
      q.pop();
      if (tokens[i] != "#") {
        node->left = new TreeNode(std::stoi(tokens[i]));
        q.push(node->left);
      }
      ++i;
      if (tokens[i] != "#") {
        node->right = new TreeNode(std::stoi(tokens[i]));
        q.push(node->right);
      }
      ++i;
    }
    return root;
  }
};

std::string toList(TreeNode *root) {
  std::vector<std::string> out;
  std::queue<TreeNode *> q;
  q.push(root);
  while (!q.empty()) {
    TreeNode *node = q.front();
    q.pop();
    if (node) {
      out.push_back(std::to_string(node->val));
      q.push(node->left);
      q.push(node->right);
    } else {
      out.push_back("null");
    }
  }
  while (!out.empty() && out.back() == "null")
    out.pop_back();
  std::string s = "[";
  for (size_t i = 0; i < out.size(); ++i) {
    if (i)
      s += ", ";
    s += out[i];
  }
  return s + "]";
}

int main() {
  Codec c;
  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);
  root->right->left = new TreeNode(4);
  root->right->right = new TreeNode(5);
  std::string data = c.serialize(root);
  std::cout << data << "\n";
  std::cout << toList(c.deserialize(data))
            << "\n"; // [1, 2, 3, null, null, 4, 5]
  std::cout << "\"" << c.serialize(c.deserialize(c.serialize(nullptr)))
            << "\"\n"; // ""
  std::cout << toList(c.deserialize(c.serialize(new TreeNode(7))))
            << "\n"; // [7]
  return 0;
}
