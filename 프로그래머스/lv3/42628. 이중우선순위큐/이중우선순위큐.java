import java.util.*;
class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        //오름차순 힙
        PriorityQueue<Integer> ascending = new PriorityQueue<>();
        //내림차순 힙
        PriorityQueue<Integer> descending = new PriorityQueue<>((a, b) -> b - a);

        for (String str : operations) {
            String[] token = str.split(" ");
            if (token[0].equals("I")) {
                ascending.add(Integer.parseInt(token[1]));
                descending.add(Integer.parseInt(token[1]));
            } else if (token[0].equals("D")) {
                if (ascending.isEmpty())
                    continue;
                else if (token[1].equals("1")) {
                    int temp = descending.poll();
                    ascending.remove(temp);
                } else if (token[1].equals("-1")) {
                    int temp = ascending.poll();
                    descending.remove(temp);
                }
            }
            System.out.println(ascending);
        }

        if (ascending.isEmpty()) {
            answer[0] = 0;
            answer[1] = 0;
        }
        else {
            answer[0] = descending.poll();
            answer[1] = ascending.poll();
        }
        return answer;
    }
}