package access;
import mypack.test;

public class demo {
    public static void main(String[] args) {
        test t = new test();
        t.read();
        t.display();
    }
}

/*
 * Output:
 * javac -d . test.java
 * javac -d . demo.java
 * java access.demo
 * Enter values of x, y, z and p
 * 1 2 3 4
 * x= 1	y= 2	z= 3	p= 4
 */