package dp;

import java.io.*;
import java.util.*;

public class retire {
    public static void main(String[] args) throws Exception{
        // 데이터 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int howLong = Integer.parseInt(br.readLine());

        int[] period = new int[howLong];
        int[] value = new int[howLong];

        for (int i = 0; i<howLong; i++){
            period[i] = Integer.parseInt(br.readLine());
            value[i] = Integer.parseInt(br.readLine());
        }

        // 뒤에서부터 앞으로 재귀
        int[] dp = new int[howLong+1];
        int maxValue=0;

        for(int i = howLong-1; i>=0; i--){
            int time = period[i] + i;

            if (time <= howLong){
                dp[i] = Math.max(maxValue, value[i] + dp[time]);
                maxValue = dp[i];
            } else dp[i] = maxValue;

        }

        System.out.println(maxValue);

    }
}
