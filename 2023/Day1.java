import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day1 {

    public static void main(String[] args) {

        int sum = 0;
        
        try {
            Scanner scanner = new Scanner(new File("input.txt"));
            
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                
                line = line.replace("one", "o1e");
                line = line.replace("two", "t2o");
                line = line.replace("three", "t3e");
                line = line.replace("four", "4");
                line = line.replace("five", "5e");
                line = line.replace("six", "6");
                line = line.replace("seven", "7n");
                line = line.replace("eight", "e8t");
                line = line.replace("nine", "n9e");
                
                System.out.println(line);
                
                int first = -1;
                int last = -1;
                for (int i = 0; i < line.length(); i++) {
                    char next = line.charAt(i);
                    if (!Character.isDigit(next)) {
                        continue;
                    }
                    int number = next - '0';
                    if (first == -1) {
                        first = number;
                    }
                    else {
                        last = number;
                    }
                }
                
                if (last == -1) {
                    last = first;
                }
                
                sum += (10*first) + last;
                
            }
            
            System.out.println(sum);
            
            scanner.close();
            
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }  
    }
}
