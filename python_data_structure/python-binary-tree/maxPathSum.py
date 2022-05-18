"""======This part is the beginning of thought============
When we try to check a path sum, the intuition is to traverse through the path.
But the path is on a tree, not on a graph, so it is very hard to go up and down....
Tree traverse should be all the way down!
And in recursion, we are going to return finally. The returning process is going up.
When going up, a parent node can get some data from its left child and right child.
We want to utilize this. (And in tree problem this often happens)

We notice that as a parent if we can know the `max-sum path that ends at its left child`. <= look at here
and as a parent if we can know the `max-sum path that ends at its right child`. <= look at here
If we know them, it will be very helpful because:

"Left path - parent - right path" this is a new path
"left path - parent", this is a new path
"parent - right path", this is a new path
"parent only", this is also a new path
there are 4 types of path formed in this parent!
Compare them and select the max one to update global answer
Compare them and select the max from 2,3,4 to return to this parent's parent.
(why 2,3,4? look at the bold parts above)"""

class Solution1:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # base case of recursion
        self.maxPathSum = float('-inf')
        self.helper(root)
        return self.maxPathSum
    def helper(self, root):
        if (not root):
            # base case of recursion
            return float('-inf')
        # recursively do down left and right subtree
        leftPathSum = self.helper(root.left)
        rightPathSum = self.helper(root.right)
        # path down left and down right could be all negatively impacting sum on top of root 
        curMaxPath = max(root.val + leftPathSum, root.val + rightPathSum, root.val)
        # definition of a "path sum" regardless which order to traverse
        curTreePathSum = root.val + leftPathSum + rightPathSum        
        # we only consider current tree path sum to calculate max path sum
        # we should not use it to calculate the max path, because its a tree and cannot
        # contribute to the recurrsive path that we are building
        self.maxPathSum = max(self.maxPathSum, curMaxPath, curTreePathSum)
        return curMaxPath


class Solution2:
    def maxPathSum(self, root: 'TreeNode') -> int:        
        ans = float("-inf")        
        def getMaxPathSum(node):
            nonlocal ans
            if not node:
                return float("-inf")
            left_sum = getMaxPathSum(node.left)
            right_sum = getMaxPathSum(node.right)
            ans = max(max([0,left_sum, right_sum, left_sum+right_sum])+node.val, ans)            
            return max([left_sum,right_sum,0])+node.val            
        getMaxPathSum(root)
        return ans   