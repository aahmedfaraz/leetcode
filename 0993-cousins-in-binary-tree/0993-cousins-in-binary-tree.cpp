class Solution {
public:
    void dfs(TreeNode* node, TreeNode* parent, int depth,
             int x, int y,
             int& depthX, int& depthY,
             TreeNode*& parentX, TreeNode*& parentY) {

        if (!node) return;

        if (node->val == x) {
            depthX = depth;
            parentX = parent;
        }

        if (node->val == y) {
            depthY = depth;
            parentY = parent;
        }

        dfs(node->left, node, depth + 1,
            x, y, depthX, depthY, parentX, parentY);

        dfs(node->right, node, depth + 1,
            x, y, depthX, depthY, parentX, parentY);
    }

    bool isCousins(TreeNode* root, int x, int y) {
        int depthX = -1, depthY = -1;
        TreeNode *parentX = nullptr, *parentY = nullptr;

        dfs(root, nullptr, 0, x, y,
            depthX, depthY, parentX, parentY);

        return depthX == depthY && parentX != parentY;
    }
};