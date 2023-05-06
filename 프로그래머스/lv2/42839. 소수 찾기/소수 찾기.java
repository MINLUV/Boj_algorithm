import java.util.HashSet;
import java.util.Iterator;

class Solution {
    public static HashSet<Integer> set = new HashSet<>();
    
    public boolean isprime(int num){
        if(num == 0 || num == 1) return false;
        int prime = (int)Math.sqrt(num);
        System.out.println("prime "+prime);
        for(int i = 2 ; i <= prime ; i++){
            if(num % i == 0){
                return false;
            }
        }
        return true;
    }
    
    public void recursive(String comb,String numbers){
        
        if(!comb.equals("")){
            set.add(Integer.valueOf(comb));
        }
        // 기저부분
        for (int i =0 ; i < numbers.length() ; i++){
            recursive(comb+numbers.charAt(i), numbers.substring(0,i) + numbers.substring(i+1));
        }
           
        //변화 부분
        
    }
    public int solution(String numbers) {
        int answer = 0;
        
        recursive("",numbers);
        
        Iterator<Integer> it = set.iterator();
        
        
        
        while(it.hasNext()){
            int num = it.next();
            
            if(isprime(num)){
                answer++;
            }
        }
        
        
        return answer;
    }
}