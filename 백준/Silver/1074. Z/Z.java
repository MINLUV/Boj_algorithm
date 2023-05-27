import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int count = 0; // 칸의 방문 순서를 저장하는 변수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int r = Integer.parseInt(input[1]);
        int c = Integer.parseInt(input[2]);

        int size = (int) Math.pow(2, N); // 2차원 배열의 크기

        solve(size, r, c);

        System.out.println(count);
    }

    public static void solve(int size, int r, int c) {
        if (size == 1) {
            return;
        }

        int half = size / 2;

        // 왼쪽 위 영역
        if (r < half && c < half) {
            solve(half, r, c);
        }
        // 오른쪽 위 영역
        else if (r < half && c >= half) {
            count += half * half;
            solve(half, r, c - half);
        }
        // 왼쪽 아래 영역
        else if (r >= half && c < half) {
            count += 2 * half * half;
            solve(half, r - half, c);
        }
        // 오른쪽 아래 영역
        else {
            count += 3 * half * half;
            solve(half, r - half, c - half);
        }
    }
}
