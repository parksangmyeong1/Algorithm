package ch01;

import java.util.*;

public class No10430{
    public static void main(String[] args)
    {
        
        Scanner sc = new Scanner(System.in);
        
        int a,b,c;
        
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        
        int num1 = (a+b)%c;
        int num2 = ((a%c)+(b%c))%c;
        int num3 = (a*b)%c;
        int num4 = ((a%c)*(b%c))%c;
        
        System.out.println(num1);
        System.out.println(num2);
        System.out.println(num3);
        System.out.println(num4);
    }
}