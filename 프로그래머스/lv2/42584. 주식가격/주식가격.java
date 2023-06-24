import java.util.*;
class Solution {
    public int[] solution(int[] prices) {
        for (int i = 0; i < prices.length; i++) {
            int j = i + 1;
            // 뒤에 주식가격이 떨어질때까지 탐색
            if (j <= prices.length - 1) {
                while (prices[i] <= prices[j]) {
                    if (j >= prices.length - 1)
                        break;
                    j++;
                }
            }
            // 주식가격이 떨어질때까지의 위치를 값으로 넣음
            prices[i] = j - i;
            
        }
        prices[prices.length-1] = 0;
        
        return prices;
    }
}