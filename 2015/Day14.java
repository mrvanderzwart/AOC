import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Day14 {
    
    public static void main(String[] args) {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            int maximum = 0;
            int gameTime = 2503;
            while ((line = bufferedReader.readLine()) != null) {
                String[] split = line.split(" ");

                int distance = Integer.parseInt(split[3]);
                int time = Integer.parseInt(split[6]);
                int rest = Integer.parseInt(split[13]);

                int nRuns = gameTime / (time+rest);

                int totalDistance = nRuns * time * distance;

                int secondsLeft = gameTime - (nRuns * (time+rest));
                totalDistance += (Math.min(secondsLeft, time) * distance);

                if (totalDistance > maximum) 
                    maximum = totalDistance;
            }

            System.out.println(maximum);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}