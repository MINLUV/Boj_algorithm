import java.util.*;
class Solution {
    static int max;
    static int[][] visited;
    public void binomialCoefficient(int[][] triangle) {
        visited[0][0] = triangle[0][0];

        // 2개의 부모노드중에서 큰 값을 자식이 내려받는다. 부모노드가 있어야 하므로 i = 1 부터 진행
        for (int i = 1; i < triangle.length; i++) {
            for (int j = 0; j <= i; j++) {
                // 맨 왼쪽 또는 오른쪽 노드일 경우 부모가 하나이므로 하나만 받는다.
                if (j == 0) {
                    visited[i][j] = visited[i - 1][j]+triangle[i][j];
                } else if (j == i) {
                    visited[i][j] = visited[i - 1][j - 1]+triangle[i][j];
                } else {
                    visited[i][j] = Math.max(visited[i - 1][j - 1], visited[i - 1][j]) + triangle[i][j];
                }
                //System.out.println(Arrays.deepToString(visited));
            }
        }
    }
    
    public int solution(int[][] triangle) {
        visited = new int[triangle.length][];    
        for (int i = 0; i < triangle.length; i++) {
            visited[i] = new int[triangle[i].length];
            Arrays.fill(visited[i], Integer.MIN_VALUE);
        }
        
        binomialCoefficient(triangle);

        for (int i = 0; i < triangle.length; i++)
            max = Math.max(max, visited[triangle.length-1][i]);
        return max;
    }
}