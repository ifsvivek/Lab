import java.io.*;

class CRC {
    public static void main(String[] args) throws IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        int[] message;
        int[] gen;
        int[] appMessage;
        int[] rem;
        int[] transMessage;
        int messageBits, genBits, totalBits;

        System.out.println("\nEnter number of bits in message: ");
        messageBits = Integer.parseInt(br.readLine());
        message = new int[messageBits];

        System.out.println("\nEnter message bits: ");
        for (int i = 0; i < messageBits; i++)
            message[i] = Integer.parseInt(br.readLine());

        System.out.println("\nEnter number of bits in generator: ");
        genBits = Integer.parseInt(br.readLine());
        gen = new int[genBits];

        System.out.println("\nEnter generator bits: ");
        for (int i = 0; i < genBits; i++)
            gen[i] = Integer.parseInt(br.readLine());

        totalBits = messageBits + genBits - 1;
        appMessage = new int[totalBits];
        rem = new int[totalBits];
        transMessage = new int[totalBits];

        for (int i = 0; i < message.length; i++)
            appMessage[i] = message[i];

        System.out.print("\nMessage bits are: ");
        for (int i = 0; i < messageBits; i++)
            System.out.print(message[i]);

        System.out.print("\nGenerator bits are: ");
        for (int i = 0; i < genBits; i++)
            System.out.print(gen[i]);

        System.out.print("\nAppended message is: ");
        for (int i = 0; i < appMessage.length; i++)
            System.out.print(appMessage[i]);

        for (int j = 0; j < appMessage.length; j++)
            rem[j] = appMessage[j];

        rem = computeCRC(appMessage, gen, rem);

        for (int i = 0; i < appMessage.length; i++)
            transMessage[i] = (appMessage[i] ^ rem[i]);

        System.out.println("\nTransmitted message from the transmitter is: ");
        for (int i = 0; i < transMessage.length; i++)
            System.out.print(transMessage[i]);

        System.out.println("\nEnter received message of " + totalBits + " bits at receiver end: ");
        for (int i = 0; i < transMessage.length; i++)
            transMessage[i] = Integer.parseInt(br.readLine());

        System.out.println("\nReceived message is: ");
        for (int i = 0; i < transMessage.length; i++)
            System.out.print(transMessage[i]);

        for (int j = 0; j < transMessage.length; j++)
            rem[j] = transMessage[j];

        rem = computeCRC(transMessage, gen, rem);

        for (int i = 0; i < rem.length; i++) {
            if (rem[i] != 0) {
                System.out.println("\nThere is an error in the received message!!!");
                break;
            }
            if (i == rem.length - 1)
                System.out.println("\nThere is no error in the received message!!!");
        }
    }

    static int[] computeCRC(int[] appMessage, int[] gen, int[] rem) {
        int current = 0;
        while (true) {
            for (int i = 0; i < gen.length; i++)
                rem[current + i] = (rem[current + i] ^ gen[i]);

            while (rem[current] == 0 && current != rem.length - 1)
                current++;

            if ((rem.length - current) < gen.length)
                break;
        }
        return rem;
    }
}