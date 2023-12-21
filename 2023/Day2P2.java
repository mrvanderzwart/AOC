import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.HashMap;

public class Day2P2 {

    public static int minimumMultiplied(String[] split) {
    
        HashMap<String, Integer> minimum = new HashMap<String, Integer>();
        
        minimum.put("red", 0);
        minimum.put("blue", 0);
        minimum.put("green", 0);
    
        for (int i = 2; i < split.length; i += 2) {
            String color = split[i+1].replaceAll("[^a-zA-Z0-9]", "");
            if (Integer.valueOf(split[i]) > minimum.get(color)) {
                minimum.put(color, Integer.valueOf(split[i]));
            }
        }
    
        return minimum.get("red")*minimum.get("green")*minimum.get("blue");
    }

    public static void main(String[] args) {
    
        try {
            Scanner scanner = new Scanner(new File("input.txt"));
            
            int sum = 0;
            
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();           
                String[] split = line.split("\\s+");
                
                sum += minimumMultiplied(split);
            }
            
            System.out.println(sum);
            
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }  
    }

}
