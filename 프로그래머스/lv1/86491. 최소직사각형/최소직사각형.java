import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        Integer[] longer = new Integer[sizes.length];
        Integer[] shorter = new Integer[sizes.length];
        // 가로세로중 큰 수를 longer에 짧은 수를 shorter 에 넣는다.
        for (int i = 0; i < sizes.length; i++) {
            if (sizes[i][0] > sizes[i][1]) {
                longer[i] = sizes[i][0];
                shorter[i] = sizes[i][1];
            } else {
                longer[i] = sizes[i][1];
                shorter[i] = sizes[i][0];
            }
        }
        int answer = 0;
        answer = Arrays.stream(longer).max(Integer::compare).get() * Arrays.stream(shorter).max(Integer::compare).get();;
        return answer;
    }
}