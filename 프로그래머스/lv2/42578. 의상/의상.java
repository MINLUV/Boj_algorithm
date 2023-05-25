import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> map = new HashMap<>();
        String type;
        for (String[] cloth : clothes) {
            type = cloth[1];
            map.put(type, map.getOrDefault(type, 0) + 1);
        }
        Iterator<Integer> it = map.values().iterator();
        
        int answer = 1;
        
        while(it.hasNext()){
            answer *= it.next()+1;
        }
        return answer-1;
    }
}
