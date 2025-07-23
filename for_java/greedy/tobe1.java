package greedy;

import java.util.*;

public class tobe1 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int result = 0;

        while (n != 1){
            result += 1;
            if (n % k == 0){
                n /= k;
            } else {
                n -= 1;
            }
        }

        System.out.println(result);
    }
}
