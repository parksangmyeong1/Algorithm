package ch02;

import java.util.*;

public class No14681{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        
        int a = s.nextInt();
        int b = s.nextInt();
        
        System.out.printf(a>0&&b>0 ? "1" : a<0&&b>0 ? "2" : a<0&&b<0 ? "3" : "4");
    }
}