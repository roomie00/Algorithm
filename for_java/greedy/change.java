package greedy;

import java.util.*;

public class change {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] coins = {500, 100, 50, 10};
        int count = 0;

        for (int coin : coins) {
            count += n / coin;
            n %= coin;
        }

        System.out.println(count);
    }
}
