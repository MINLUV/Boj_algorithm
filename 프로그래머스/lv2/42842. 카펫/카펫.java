import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
            
        for (int i =1 ; i<=yellow ; i++ ){
            // yellow 의 약수를 구하는 과정
            if(yellow % i == 0){
                int column  = yellow/i ;
                if( ((column+2) * (i+2)) - yellow == brown  ){
                    answer[0] = column+2;
                    answer[1] = i+2;
                    return answer;
                }
            }
        }
        
        return answer;
    }
}