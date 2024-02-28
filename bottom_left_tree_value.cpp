/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    //global variables to keep track of max depth and value through recursion
    int max = 0;
    int maxv = 0;

    //driver function
    int findBottomLeftValue(TreeNode* root) {
        maxv = root->val;
        meatAndPotatoes(root, 0);
        return maxv;
    }

    void meatAndPotatoes(TreeNode* node, int cur){
        if (node == NULL){return;}
        if (node->left == NULL && node->right == NULL){
            //if no children, check if we have reached a new depth and update globals if so
            if(cur > max){
                cout << node->val << endl;
                max = cur;
                maxv = node->val;
            }
            return;
        }
        return meatAndPotatoes(node->left, cur+1), meatAndPotatoes(node->right, cur+1);
    }
};