package greedy;

import java.util.*;

public class big_number {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
        int[] numbers = new int[n];
        for (int i = 0; i<n; i++){
            numbers[i] = sc.nextInt();
        }

        Arrays.sort(numbers);
        int iter_num = m/(k+1);
        int result = numbers[n-2]*iter_num + numbers[n-1]*(m-iter_num);
        System.out.println(result);
    }
}
