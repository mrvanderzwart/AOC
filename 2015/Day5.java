import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

class Day5 {

    public static String filePath = "input.txt";

    public static List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u');
    public static List<String> forbidden = Arrays.asList("ab", "cd", "pq", "xy");

    public static boolean checkProperty1P1(String line) {
        int count = 0;
        for (int i = 0; i < line.length(); i++) {
            if (vowels.contains(line.charAt(i))) count++;

            if (count >= 3) {
                return true;
            }
        }

        return false;
    }

    public static boolean checkProperty2P1(String line) {
        for (int i = 0; i < line.length()-1; i++) {
            if (line.charAt(i) == line.charAt(i+1)) {
                return true;
            }
        }

        return false;
    }

    public static boolean checkProperty3P1(String line) {
        for (int i = 0; i < line.length(); i++) {
            for (String searchString : forbidden) {
                if (line.contains(searchString))
                    return false;
            }
        }

        return true;
    }

    public static boolean checkProperty1P2(String line) {
        Character ch1;
        Character ch2;
        for (int i = 0; i < line.length()-1; i++) {
            ch1 = line.charAt(i);
            ch2 = line.charAt(i+1);
            for (int j = i+2; j < line.length()-1; j++) {
                if (ch1 == line.charAt(j) && 
                    ch2 == line.charAt(j+1))
                    return true;
            }
        }

        return false;
    }

    public static boolean checkProperty2P2(String line) {
        for (int i = 0; i < line.length()-2; i++) {
            if (line.charAt(i) == line.charAt(i+2)) {
                return true;
            }
        }

        return false;
    }

    public static void part1() {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath))) {
            int count = 0;
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                if (checkProperty1P1(line) &&
                    checkProperty2P1(line) &&
                    checkProperty3P1(line))
                    count++;
            }

            System.out.println(count);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void part2() {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath))) {
            int count = 0;
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                if (checkProperty1P2(line) &&
                    checkProperty2P2(line))
                    count++;
            }

            System.out.println(count);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        part1();
        part2();
    }
    
}