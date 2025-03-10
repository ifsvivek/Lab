package com.example.lab2;

import org.apache.commons.lang3.StringUtils;

public class App {
    public static void main(String[] args) {
        String str = "Hello World!";
        System.out.println("Trimmed :" + StringUtils.trim(str));
        System.out.println("Is empty: " + StringUtils.isEmpty(str));
        System.out.println("Is blank: " + StringUtils.isBlank(str));
        System.out.println("Reversed: " + StringUtils.reverse(str));
        System.out.println("Uppercase: " + StringUtils.upperCase(str));
    }
}