import java.io.*;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(bf.readLine());

        int[] numbers = new int[N];
        String[] numInputs = bf.readLine().split(" ");

        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(numInputs[i]);
        }

        // numbers를 오름차순 정렬한다.
        Arrays.sort(numbers);

        int M = Integer.parseInt(bf.readLine());
        String[] targetInputs = bf.readLine().split(" ");

        for (String target : targetInputs) {
            int targetNum = Integer.parseInt(target);

            // 이분 탐색으로 targetNum이 numbers에 있는지 확인한다.
            int start = 0;
            int end = N - 1;
            boolean isFound = false;

            while (start <= end) {
                int mid = (start + end) / 2;

                if (targetNum < numbers[mid]) {
                    end = mid - 1;
                } else if (targetNum > numbers[mid]) {
                    start = mid + 1;
                } else {
                    isFound = true;
                    break;
                }
            }

            System.out.println((isFound) ? "1" : "0");
        }

    }
}
