package ch01;

import java.util.*;

public class No2588{
    public static void main(String[] args)
    {
        
        Scanner s = new Scanner(System.in);
        
        int a,b,c;
        
        a = s.nextInt();
        b = s.nextInt();
        
        
        System.out.println(a*(b%10));
        System.out.println(a*(b/10%10));
        System.out.println(a*(b/100%10));
        System.out.println(a*b);
    }
}