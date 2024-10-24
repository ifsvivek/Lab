public class SlidingWindowProtocol {
    private final int windowSize;
    private int sendBase;
    private int nextSeqNum;

    public SlidingWindowProtocol(int windowSize) {
        this.windowSize = windowSize;
        this.sendBase = 0;
        this.nextSeqNum = 0;
    }

    public void sendData(char[] data) {
        while (nextSeqNum < sendBase + windowSize && nextSeqNum < data.length) {
            Packet packet = new Packet(nextSeqNum, data[nextSeqNum]);
            simulateSendPacket(packet);
            nextSeqNum++;
        }
    }

    public void receiveAck(int ackNum) {
        sendBase = ackNum + 1;
    }

    private void simulateSendPacket(Packet packet) {
        System.out.println("Sending packet: " + packet);
    }

    private void simulateAckPacket(int ackNum) {
        System.out.println("Received ack: " + ackNum);
        receiveAck(ackNum);
    }

    private static class Packet {
        private final int seqNum;
        private final char data;

        public Packet(int seqNum, char data) {
            this.seqNum = seqNum;
            this.data = data;
        }

        public String toString() {
            return "Packet{seqNum=" + seqNum + ", data=" + data + "}";
        }
    }

    public static void main(String[] args) {
        char[] data = { 'a', 'b', 'c', 'd', 'e', 'f', 'g' };
        SlidingWindowProtocol swp = new SlidingWindowProtocol(4);
        swp.sendData(data);
        swp.simulateAckPacket(0);
        swp.simulateAckPacket(1);
        swp.simulateAckPacket(2);
        swp.simulateAckPacket(3);
    }
}