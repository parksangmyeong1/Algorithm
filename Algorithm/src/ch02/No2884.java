package ch02;

import java.util.*;

public class No2884{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        
        int H = s.nextInt();
        int M = s.nextInt();
        
        if (H==0&&M-45<0){
            System.out.printf("%d %d", 23,60+M-45);
        }
        else if(M-45<0){
            System.out.printf("%d %d", H-1,60+M-45);
        }
        else{
            System.out.printf("%d %d", H, M-45);
        }
    }
}