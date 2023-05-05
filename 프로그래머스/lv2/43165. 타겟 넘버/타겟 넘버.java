class Solution {
    int[] numbers;
    int target;
    int count; 
    
    public void dfs(int index, int total ){
        // 1. 기저 부분
        if(index >= numbers.length){
            if(total == target){
                count++;
            }
            return;
        }
        
        // 2. 반복 진행될 코드
        dfs(index + 1,total + numbers[index]);
        dfs(index + 1,total - numbers[index]);
        
    }
    public int solution(int[] numbers, int target) {
        int answer = 0;
        this.numbers = numbers;
        this.target = target;
        this.count = 0;
        dfs(0,0);
        answer = count;
        return answer;
    }
}