import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class Day1 {

    public static String filePath = "input.txt";

    public static void part1() {
        try (FileReader fileReader = new FileReader(filePath);
            BufferedReader bufferedReader = new BufferedReader(fileReader)) {

            int floor = 0;
            int charCode;
            while ((charCode = bufferedReader.read()) != -1) {
                char character = (char) charCode;

                if (character == '(') 
                    floor++;
                else if (character == ')')
                    floor--;
            }

            System.out.println(floor);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void part2() {
        try (FileReader fileReader = new FileReader(filePath);
            BufferedReader bufferedReader = new BufferedReader(fileReader)) {

            int floor = 0;
            int position = 1;
            int charCode;
            while ((charCode = bufferedReader.read()) != -1) {
                char character = (char) charCode;

                if (character == '(') 
                    floor++;
                else if (character == ')')
                    floor--;

                if (floor < 0)
                    break;

                position++;
            }

            System.out.println(position);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        part1();
        part2();
    }
    
}