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
    bool isEvenOddTree(TreeNode* root) {
        //BFS traversal
        if(root == NULL){return false;}

        queue<queue<TreeNode*>> q; //create a queue of queues to be able to track which level we are on
        queue<TreeNode*> rq; //create queue for root level
        rq.push(root);
        q.push(rq);
        int level = 0;

        while(q.empty() == false){

            queue<TreeNode*> curq = q.front(); //get queue for current level
            q.pop();
            queue<TreeNode*> lq; //temp queue to store child nodes
            int prev = -1; //keep track of previous node for increasing/decreasing order check

            while(curq.empty() == false){

                TreeNode* node = curq.front();
                curq.pop();

                switch(level % 2){
                    case 0:
                        if(node->val % 2 == 0){return false;} //odd check
                        if(prev != -1 && prev >= node->val){return false;} //increasing order check
                        if(node->left != NULL){
                            lq.push(node->left);
                        }
                        if(node->right != NULL){
                            lq.push(node->right);
                        }
                        break;

                    case 1:
                        if(node->val % 2 != 0){return false;} //even check
                        if(prev != -1 && prev <= node->val){return false;} //decreasing order check
                        if(node->left != NULL){
                            lq.push(node->left);
                        }
                        if(node->right != NULL){
                            lq.push(node->right);
                        }
                        break;
                }
                prev = node->val;
            }

            if(lq.empty() == false){q.push(lq);} //push child queue into level queue if populated
            level++; //increment level
        }
        return true;
    }
};