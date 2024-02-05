import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Day12 {

    static String parseInput(String input) {
        String pattern = "[\\{\\}\\[\\]\" \"]";
        String result = input.replaceAll(pattern, "");
        result = result.replace(":", ",");

        return result;
    }

    static void part1(String input) {
        input = parseInput(input);
        String[] split = input.split(",");
        int sum = 0;
        for (String wd : split) {
            try {
                sum += Integer.parseInt(wd);
            } catch (NumberFormatException e) {}
        }
        System.out.println(sum);
    }

    public static void main(String[] args) {
        
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader("input.txt"))) {
            String input = bufferedReader.readLine();
            part1(input);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}