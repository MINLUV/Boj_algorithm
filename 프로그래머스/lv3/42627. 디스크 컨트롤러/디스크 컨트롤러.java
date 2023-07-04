import java.util.*;
class Solution {
    public int solution(int[][] jobs) {
        int time = 0, endpoint = 0, index = 0 , i = 0; 
        PriorityQueue<int[]> heap = new PriorityQueue<>((o1, o2)->o1[1] - o2[1]);
        Arrays.sort(jobs, Comparator.comparingInt((int[] o) -> o[0]));

        System.out.println(Arrays.deepToString(jobs));

        while(i < jobs.length) {
            while (index < jobs.length && jobs[index][0] <= endpoint) {
                heap.add(jobs[index++]);
                
            }

            if(heap.isEmpty())
                endpoint = jobs[index][0];

            else {
                int[] temp = heap.poll();
                time += temp[1] + endpoint - temp[0];
                endpoint += temp[1];
                i++;
            }
            System.out.println(time);
        }
        return (int) time / jobs.length;
    }
}