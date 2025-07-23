package dfsbfs;

import java.util.*;

// 프로그래머스 "단어변환"
// https://school.programmers.co.kr/learn/courses/30/lessons/43163
class ChangeWord {
    private static Queue<Map.Entry<String, Integer>> q = new LinkedList<>();

    public static int solution(String begin, String target, String[] words) {
        int len = words.length;

        // words에 target이 없다면 0 반환
        for(int i=0; i<len; i++){
            if(words[i].equals(target)){
                break;
            } else if(i == len-1){
                return 0;
            }
        }

        for(int i=0; i<len; i++){
            if(compareString(begin, words[i])){
                q.offer(new AbstractMap.SimpleEntry<>(words[i], 1));
            }
        }

        while(!q.isEmpty()){
            Map.Entry<String, Integer> now = q.poll();

            if (now.getKey().equals(target)){
                return now.getValue();
            }

            for (int i=0; i<len; i++){
                if(compareString(now.getKey(), words[i])){
                    q.offer(new AbstractMap.SimpleEntry<>(words[i], now.getValue()+1));
                }
            }
        }

        return 0;
    }

    // 단어 철자 비교용 함수
    public static Boolean compareString(String begin, String word){
        int same = 0;
        int word_len = word.length();

        for(int i=0; i<word_len; i++){
            if(begin.charAt(i) == word.charAt(i)){
                same++;
            }

            // 철자가 하나만 다른 경우에만 true 리턴
            if(same == word_len-1){
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args){
        String begin = "hit";
        String target = "cog";
        String[] words = {"hot", "dot", "dog", "lot", "log", "cog"};

        System.out.println(solution(begin, target, words));
    }
}

