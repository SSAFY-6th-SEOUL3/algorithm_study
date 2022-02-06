import java.util.ArrayList;
import java.util.Scanner;

public class BOJ10773 {
    final static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        final int LIMIT = 100000;
        int K = scanner.nextInt();

        ArrayList<Integer> data = new ArrayList<Integer>(LIMIT);

        int sum = 0;
        for (int i = 0; i < K; i++) {
            int n = scanner.nextInt();

            if (n == 0) {
                sum -= (int) data.get(data.size() - 1); // data[-1]
                data.remove(data.size() - 1); // pop()
            } else {
                sum += n;
                data.add(n);
            }
        }

        System.out.println(sum);
    }
}