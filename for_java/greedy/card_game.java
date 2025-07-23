package greedy;
import java.util.*;

public class card_game {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] cards = new int[n];

        int result = 0;
        for(int i = 0; i<n; i++){
            int min_num = 10001;
            for (int j = 0; j<m; j++) {
                min_num = Math.min(min_num, sc.nextInt());
            }
            result = Math.max(result, min_num);
        }

        System.out.println(result);
    }
}
