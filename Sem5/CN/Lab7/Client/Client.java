import java.io.*;
import java.net.*;
import java.nio.file.*;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the file name you want to request: ");
        String fileName = scanner.nextLine();
        if (!fileName.isEmpty()) {
            requestFileFromServer(fileName);
        }
        scanner.close();
    }

    public static void requestFileFromServer(String fileName) {
        String urlString = "http://localhost:8000/" + fileName;

        try {
            URI uri = new URI(urlString);
            URL url = uri.toURL();
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");

            int status = connection.getResponseCode();

            if (status == HttpURLConnection.HTTP_OK) {
                InputStream inputStream = connection.getInputStream();
                Path savePath = Paths.get("saved", fileName);
                Files.createDirectories(savePath.getParent());
                Files.copy(inputStream, savePath, StandardCopyOption.REPLACE_EXISTING);
                System.out.println("File saved to " + savePath.toString());
                inputStream.close();
            } else {
                System.out.println("Error: " + status + " - File not found.");
            }

            connection.disconnect();

        } catch (IOException | URISyntaxException e) {
            e.printStackTrace();
        }
    }
}