package com.example.lab2;

import junit.framework.TestCase;
import org.apache.commons.lang3.StringUtils;

public class AppTest extends TestCase {
    public void testStringUtils() {
        String input = "  Hello World!  ";
        // Test trim
        assertEquals("Hello World!", StringUtils.trim(input));
        // Test isEmpty
        assertFalse(StringUtils.isEmpty(input));
        assertTrue(StringUtils.isEmpty(""));
        // Test reverse
        assertEquals("!dlroW olleH", StringUtils.reverse(input.trim()));
        // Test upperCase
        assertEquals("HELLO WORLD!", StringUtils.upperCase(input.trim()));
    }
}
