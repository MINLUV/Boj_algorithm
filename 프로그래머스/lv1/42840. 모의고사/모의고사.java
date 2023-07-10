import java.util.*;
class Solution {
    public int[] solution(int[] answers) {  
        ArrayList<Integer> arr = new ArrayList<>();
        int[] count = { 0, 0, 0 };
        int[] firman = { 1, 2, 3, 4, 5 };
        int[] seman = { 2, 1, 2, 3, 2, 4, 2, 5 };
        int[] thman = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };

        for (int i = 0; i < answers.length; i++) {
            if (firman[i % 5] == answers[i]) {
                count[0] += 1;
            }
            if (seman[i % 8] == answers[i]) {
                count[1] += 1;
            }
            if (thman[i % 10] == answers[i]) {
                count[2] += 1;
            }
        }

        int max = Math.max(count[0], Math.max(count[1], count[2]));

        for (int i = 0; i < count.length; i++) {
            if (count[i] >= max) {
                arr.add(i+1);
            }
        }
        System.out.println(arr);
        int[] answer = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            answer[i] = arr.get(i);
        }
        return answer;
    }
}