import java.net.*;

public class DatagramExample {
    public static int serverPort = 1666;
    public static int clientPort = 1999;
    public static int buffer_size = 1024;
    public static DatagramSocket ds;

    public static void TheServer() throws Exception {
        byte[] buffer = new byte[buffer_size];
        int pos = 0;
        while (true) {
            int c = System.in.read();
            switch (c) {
                case -1:
                    System.out.println("Server Quits.");
                    return;
                case '\r':
                    break;
                case '\n':
                    ds.send(new DatagramPacket(buffer, pos, InetAddress.getLocalHost(), clientPort));
                    pos = 0;
                    break;
                default:
                    if (pos < buffer.length) {
                        buffer[pos++] = (byte) c;
                    } else {
                        System.err.println("Buffer overflow");
                        pos = 0;
                    }
            }
        }
    }

    public static void TheClient() throws Exception {
        byte[] buffer = new byte[buffer_size];
        while (true) {
            DatagramPacket p = new DatagramPacket(buffer, buffer.length);
            ds.receive(p);
            System.out.println(new String(p.getData(), 0, p.getLength()));
        }
    }

    public static void main(String args[]) throws Exception {
        if (args.length == 1) {
            ds = new DatagramSocket(serverPort);
            TheServer();
        } else {
            ds = new DatagramSocket(clientPort);
            TheClient();
        }
    }
}