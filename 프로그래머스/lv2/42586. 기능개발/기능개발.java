import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = new int[progresses.length];
        int day = 0;

        for (int i = 0; i < progresses.length; i++) {
            while (progresses[i] < 100) {
                for (int j = 0; j < progresses.length; j++) {
                    progresses[j] += speeds[j];
                }
                day++;
            }
            answer[i] = day;
        }

        ArrayList<Integer> resultList = new ArrayList<>();
        int count = 1;
        int prev = answer[0];
        for (int i = 1; i < answer.length; i++) {
            if (answer[i] > prev) {
                resultList.add(count);
                count = 1;
                prev = answer[i];
            } else {
                count++;
            }
        }
        resultList.add(count);

        int[] resultArray = new int[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            resultArray[i] = resultList.get(i);
        }

        return resultArray;
    }
}