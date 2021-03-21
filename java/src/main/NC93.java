//设计LRU缓存结构

import java.util.*;

public class NC93 {
    /**
     * lru design
     *
     * @param operators int整型二维数组 the ops
     * @param k         int整型 the k
     * @return int整型一维数组
     */
    public int[] LRU(int[][] operators, int k) {
        LruCache lruCache = new LruCache(k);
        List<Integer> list = new ArrayList<>();
        for (int[] op : operators) {
            if (op[0] == 1) {
                lruCache.set(op[1], op[2]);
            } else if (op[0] == 2) {
                int val = lruCache.get(op[1]);
                list.add(val);
            }
        }
        return list.stream().mapToInt(Integer::valueOf).toArray();
    }

    public static void main(String[] args) {
        int[][] operators=new int[][]{{1,1,1},{1,2,2},{1,3,2},{2,1},{1,4,4},{2,2}};
        int k=3;
        NC93 nc93 = new NC93();
        int[] lru = nc93.LRU(operators, k);
        System.out.println(Arrays.toString(lru));
    }

}

class LruCache{

    int capacity;
    Map<Integer, Node> map = new HashMap<>();
    Node head = new Node();
    Node tail = new Node();

    public LruCache(int capacity) {
        this.capacity=capacity;
        head.next = tail;
        tail.prev = head;
    }

    static class Node {
        int k;
        int v;
        Node next;
        Node prev;

        public Node(int v,int k) {
            this.v = v;
            this.k = k;
        }

        public Node(){}
    }

    void set(int k, int v) {
        if (map.containsKey(k)) {
            Node node = map.get(k);
            if (isFist(node)) {
                return;
            }
            moveToFirst(node);
        } else {
            if (map.size() == capacity) {
                map.remove(tail.prev.k);
                removeLast();
            }
            Node node = new Node(v, k);
            map.put(k, node);
            insertToFirst(node);
        }
    }

    int get(int k) {
        if (map.containsKey(k)) {
            Node node = map.get(k);
            moveToFirst(node);
            return node.v;
        }
        return -1;
    }

    void insertToFirst(Node node) {
        Node t = head.next;
        head.next=node;
        node.prev=head;
        node.next=t;
        t.prev=node;
    }

    void removeLast() {
        remove(tail.prev);
    }

    void moveToFirst(Node node) {
        remove(node);
        insertToFirst(node);
    }

    void remove(Node node) {
        Node prevNode=node.prev;
        Node nextNode=node.next;
        prevNode.next=nextNode;
        nextNode.prev=prevNode;
    }

    boolean isFist(Node node) {
        return head.next==node;
    }
}