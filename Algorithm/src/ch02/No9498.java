package ch02;

import java.util.*;

public class No9498{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        
        int a = s.nextInt();
        
        
        System.out.printf((a>=90) ? "A" : (a>=80) ? "B" : (a>=70) ? "C" : a>=60 ? "D" : "F");
    }
}