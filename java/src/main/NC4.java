//判断链表中是否有环

public class NC4 {

    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }
        ListNode quick = head;
        ListNode slow = head;
        while (quick != null && quick.next != null) {
            quick = quick.next.next;
            slow = slow.next;
            if (quick == slow) {
                return true;
            }
        }
        return false;
    }

}

