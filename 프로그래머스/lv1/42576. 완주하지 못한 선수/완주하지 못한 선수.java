import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        int result = 0;
        HashMap<Integer,String> map = new HashMap<>();
        
        for(int i=0; i<participant.length;i++){
            int hash = participant[i].hashCode();
            result += hash;
            map.put(hash,participant[i]);
        }
        for(int i=0; i<completion.length;i++){
            result -= completion[i].hashCode();
        }
        answer = map.get(result);
        
        return answer;
    }
}