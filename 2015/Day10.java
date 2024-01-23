import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Day10 {
    
    public static void main(String[] args) {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader("input.txt"))) {
            String number = bufferedReader.readLine();
            String result = extendString(number, 50);
            System.out.println(result.length());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String extendString(String number, int iterations) {
        if (iterations == 0) {
            return number;
        }

        StringBuilder newNumber = new StringBuilder();
        int count = 1;

        for (int i = 0; i < number.length(); i++) {
            while (i < number.length()-1 && number.charAt(i) == number.charAt(i+1)) {
                count++;
                i++;
            }

            newNumber.append(count).append(number.charAt(i));
            count = 1;
        }

        return extendString(newNumber.toString(), iterations-1);
    }
}