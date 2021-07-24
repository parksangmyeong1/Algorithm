package ch02;

import java.util.*;

public class No1330{
    public static void main(String[] args)
    {
        
        Scanner s = new Scanner(System.in);
        
        int a = s.nextInt();
        int b = s.nextInt();
        
        
        if (a>b){
            System.out.printf(">");
        }
        else if (a<b){
            System.out.printf("<");
        }
        else{
            System.out.printf("==");
        }
    }
}