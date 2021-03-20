import java.util.*;
import java.util.function.ToIntFunction;

public class NC93 {
    /**
     * lru design
     *
     * @param operators int整型二维数组 the ops
     * @param k         int整型 the k
     * @return int整型一维数组
     */
    public int[] LRU(int[][] operators, int k) {
        this.capacity = k;
        List<Integer> list = new ArrayList<>();
        head.next = tail;
        tail.prev = head;
        for (int[] op : operators) {
            if (op[0] == 1) {
                set(op[1], op[2]);
            } else if (op[1] == 2) {
                int val = get(op[1]);
                list.add(val);
            }
        }
        return list.stream().mapToInt(Integer::valueOf).toArray();
    }

    int capacity;
    Map<Integer, Integer> map = new HashMap<>();
    Node head = new Node();
    Node tail = new Node();

    class Node {
        int val;
        Node next;
        Node prev;

        public Node(int val) {
            this.val = val;
        }

        public Node(){}
    }

    void set(int k, int v) {
        if (map.entrySet().size() < k) {
            map.put(k, v);
            Node node = new Node(v);
            Node t = head.next;
            head.next=node;
            node.prev=head;
            node.next=t;
            t.prev=node;
        } else {

        }
    }

    int get(int k) {
        return k;
    }
}
