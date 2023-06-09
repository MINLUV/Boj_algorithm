import java.util.*;
class Solution {
    boolean solution(String s) {
        Stack<String> parenthese = new Stack<>();
        for (char index : s.toCharArray()) {
            // 주의사항 "" 로 쓰면 오류가 나며 '' 를 써야한다.
            if (index == '(') {
                parenthese.push("(");
            }

            else if (index == ')') {
                if (parenthese.isEmpty()) {
                    return false;
                } 
                else {
                    parenthese.pop();
                }
            }
        }

        if (parenthese.isEmpty()) {
            return true;
        } else {
            return false;
        }
    }        
}