//https://programmers.co.kr/learn/courses/30/lessons/64061 
//크레인 인형뽑기 문제(카카오 채용 문제)


import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        //Stack방법으로 바구니에 넣기 
        Stack<Integer> stack = new Stack<>();
        
        // moves의 항목만큼 반복 (크레인이 향하는 순서)
        for(int move: moves){
            for(int i = 0; i < board.length; i++){
                if(board[i][move-1] != 0){
                    if(stack.empty() == true){
                        stack.push(board[i][move-1]);   
                    }
                    else {
                        if(stack.peek() == board[i][move-1]){
                            stack.pop();
                            answer += 2;
                        }
                        else{
                            stack.push(board[i][move-1]);   
                        }
                    }
                    // 크레인으로 인형(숫자)을 뽑으면 빈칸이 되기 때문에 빈칸(0)을 넣어 준다. 
                    board[i][move-1] = 0;
                    break;
                }
            }
        }

        return answer;
    }
}
