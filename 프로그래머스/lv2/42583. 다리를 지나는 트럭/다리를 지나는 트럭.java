import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        LinkedList<Integer> queue = new LinkedList<>();
        for(int i = 0 ; i<bridge_length  ; i++)
            queue.add(0);
        int queueweight = 0;
        int count = 0;
        for (int i : truck_weights) {
            while (true) {
                
                count++;
                if (queue.size() <= bridge_length && queueweight + i <= weight+queue.peek()) {
                    queueweight += i - queue.poll();
                    queue.add(i);
                    break;
                } else {
                    queueweight -= queue.poll();
                    queue.add(0);
                }
            }
        }
        while (queueweight > 0) {
            queueweight -= queue.poll();
            count++;
            
        }
        return count;
    } 
}