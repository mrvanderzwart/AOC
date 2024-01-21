import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class Day6 {

    public static String filePath = "input.txt";

    public static boolean[][] toggleLightsP1(boolean[][] lights, boolean toggle, boolean state, int startx, int starty, int endx, int endy) {
        for (int i = starty; i <= endy; i++) {
            for (int j = startx; j <= endx; j++) {
                if (toggle) 
                    lights[i][j] = !lights[i][j];
                else    
                    lights[i][j] = state;
            }
        }

        return lights;
    }

    public static int[][] toggleLightsP2(int[][] lights, boolean toggle, boolean state, int startx, int starty, int endx, int endy) {
        for (int i = starty; i <= endy; i++) {
            for (int j = startx; j <= endx; j++) {
                if (toggle) 
                    lights[i][j] += 2;
                else if (state)
                    lights[i][j]++;
                else
                    lights[i][j] = Math.max(0, lights[i][j]-1);
            }
        }

        return lights;
    }

    public static void countLightsP1(boolean[][] lights) {
        int count = 0;
        for (int i = 0; i < lights.length; i++) {
            for (int j = 0; j < lights[i].length; j++) {
                if (lights[i][j])
                    count++;
            }
        }

        System.out.println(count);
    }

    public static void countLightsP2(int[][] lights) {
        int count = 0;
        for (int i = 0; i < lights.length; i++) {
            for (int j = 0; j < lights[i].length; j++) {
                count += lights[i][j];
            }
        }

        System.out.println(count);
    }

    public static void part1() {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath))) {
            boolean[][] lights = new boolean[1000][1000];
            String line;
            String[] start;
            String[] end;
            boolean toggle = false;
            boolean state = false;
            while ((line = bufferedReader.readLine()) != null) {
                String[] split = line.split(" ");
                if (split.length == 4) {
                    toggle = true;
                    start = split[1].split(",");
                    end = split[3].split(",");
                } else {
                    state = split[1].equals("on");
                    start = split[2].split(",");
                    end = split[4].split(",");
                }

                int startx = Integer.parseInt(start[0]);
                int starty = Integer.parseInt(start[1]);
                int endx = Integer.parseInt(end[0]);
                int endy = Integer.parseInt(end[1]);

                lights = toggleLightsP1(lights, toggle, state, startx, starty, endx, endy);
                toggle = false;
            }

            countLightsP1(lights);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void part2() {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath))) {
            int[][] lights = new int[1000][1000];
            String line;
            String[] start;
            String[] end;
            boolean toggle = false;
            boolean state = false;
            while ((line = bufferedReader.readLine()) != null) {
                String[] split = line.split(" ");
                if (split.length == 4) {
                    toggle = true;
                    start = split[1].split(",");
                    end = split[3].split(",");
                } else {
                    state = split[1].equals("on");
                    start = split[2].split(",");
                    end = split[4].split(",");
                }

                int startx = Integer.parseInt(start[0]);
                int starty = Integer.parseInt(start[1]);
                int endx = Integer.parseInt(end[0]);
                int endy = Integer.parseInt(end[1]);

                lights = toggleLightsP2(lights, toggle, state, startx, starty, endx, endy);
                toggle = false;
            }

            countLightsP2(lights);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        part1();
        part2();
    }
    
}