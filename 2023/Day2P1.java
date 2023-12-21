import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.HashMap;

public class Day2 {

    public static boolean checkGame(String[] split, HashMap<String, Integer> maximum) {
        for (int i = 2; i < split.length; i += 2) {
            String color = split[i+1].replaceAll("[^a-zA-Z0-9]", "");
            if (Integer.valueOf(split[i]) > maximum.get(color)) {
                return false;
            }
        }
    
        return true;
    }

    public static void main(String[] args) {
    
        try {
            Scanner scanner = new Scanner(new File("input.txt"));
            
            HashMap<String, Integer> maximum = new HashMap<String, Integer>();
    
            maximum.put("red", 12);
            maximum.put("blue", 14);
            maximum.put("green", 13);
            
            int sum = 0;
            
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();           
                String[] split = line.split("\\s+");
                int game_num = Integer.valueOf(split[1].replace(":", ""));
                
                if (checkGame(split, maximum)) {
                    sum += game_num;
                }
            }
            
            System.out.println(sum);
            
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }  
    }

}
