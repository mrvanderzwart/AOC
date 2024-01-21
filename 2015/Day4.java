import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

class Day4 {

    public static String filePath = "input.txt";

    public static void part1(int start) {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath))) {

            int number = 0;
            String key;
            key = bufferedReader.readLine();
            while(true) {
                String hashString = key + String.valueOf(number);

                try {
                    MessageDigest md = MessageDigest.getInstance("MD5");
        
                    md.update(hashString.getBytes());
        
                    byte[] hashBytes = md.digest();
        
                    StringBuilder hash = new StringBuilder();
                    for (byte b : hashBytes) {
                        String hex = String.format("%02x", b);
                        hash.append(hex);
                    }
        
                    boolean found = true;
                    for (int i = 0; i < start; i++) {
                        if (hash.charAt(i) != '0') {
                            found = false;
                            break;
                        }
                    }

                    if (found) break;

                    number++;
        
                } catch (NoSuchAlgorithmException e) {
                    e.printStackTrace();
                }
            }

            System.out.println(number);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        part1(5);
        part1(6);
    }
    
}