import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

public class Day3P1 {

    public static String[] readNumbers(String line, int j) {

        while (Character.isDigit(line.charAt(j))) {
            j++;
            if (j >= line.length())
                break;
        }
        
        int base = 1;
        int number = 0;
        StringBuilder newString = new StringBuilder(line);

        while (j - 1 >= 0 && Character.isDigit(line.charAt(j-1))) {
            number += base*(line.charAt(j-1)-'0');
            base *= 10;
            newString.setCharAt(j-1, '.');
            j--;
        }

        String[] result = new String[2]; 
        result[0] = Integer.toString(number);
        result[1] = newString.toString();
        
        return result;
    }

    public static void main(String[] args) {
    
        try {
            Scanner scanner = new Scanner(new File("input.txt"));
            
            ArrayList<String> grid = new ArrayList<String>();
            
            while (scanner.hasNextLine()) {
                grid.add(scanner.nextLine());
            }

            int sum = 0;

            String[] result = new String[2];
                
            for (int i = 0; i < grid.size(); i++)
            {
                for (int j = 0; j < grid.get(i).length(); j++) {
                    if (!Character.isDigit(grid.get(i).charAt(j)) && Character.compare(grid.get(i).charAt(j), '.') != 0) {
                        if (i > 0) {
                            result = readNumbers(grid.get(i-1), j);
                            sum += Integer.parseInt(result[0]);
                            grid.set(i-1, result[1]);
                            if (j + 1 < grid.get(i-1).length())
                                result = readNumbers(grid.get(i-1), j+1);
                                sum += Integer.parseInt(result[0]);
                                grid.set(i-1, result[1]);
                        }   
                        if (i + 1 < grid.size()) {
                            result = readNumbers(grid.get(i+1), j);
                            sum += Integer.parseInt(result[0]);
                            grid.set(i+1, result[1]);
                            if (j + 1 < grid.get(i+1).length())
                                result = readNumbers(grid.get(i+1), j+1);
                                sum += Integer.parseInt(result[0]);
                                grid.set(i+1, result[1]);
                        }
                        
                        result = readNumbers(grid.get(i), j);
                        sum += Integer.parseInt(result[0]);
                        grid.set(i, result[1]);
                        if (j + 1 < grid.get(i).length()) 
                            result = readNumbers(grid.get(i), j+1); 
                            sum += Integer.parseInt(result[0]);
                            grid.set(i, result[1]);                       
                    }
                }
            }
            
            System.out.println(sum);
            
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }  
    }
}
