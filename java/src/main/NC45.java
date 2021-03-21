import java.util.ArrayList;
import java.util.List;

public class NC45 {
    /**
     *
     * @param root TreeNode类 the root of binary tree
     * @return int整型二维数组
     */
    public int[][] threeOrders (TreeNode root) {
        order(root);
        int[] preOrderArray=preOrderList.stream().mapToInt(x -> x).toArray();
        int[] inOrderArray=inOrderList.stream().mapToInt(x -> x).toArray();
        int[] postOrderArray=postOrderList.stream().mapToInt(x -> x).toArray();
        return new int[][]{preOrderArray,inOrderArray,postOrderArray};
    }

    List<Integer> preOrderList = new ArrayList<>();
    List<Integer> inOrderList = new ArrayList<>();
    List<Integer> postOrderList = new ArrayList<>();

    void order(TreeNode root) {
        if (root == null) {
            return;
        }
        preOrderList.add(root.val);
        order(root.left);
        inOrderList.add(root.val);
        order(root.right);
        postOrderList.add(root.val);
    }

}
