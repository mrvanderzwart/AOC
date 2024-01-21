import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Day2 {

    public static String filePath = "input.txt";

    public static int surfaceArea(int l, int w, int h) {
        int area = 2*l*w + 2*w*h + 2*h*l;

        area += Math.min(Math.min(l*w, w*h), h*l);

        return area;
    }

    public static int ribbon(String[] sizes) {
        int area = 0;
        List<Integer> intSizes = new ArrayList<>();
        for (String str : sizes) {
            intSizes.add(Integer.parseInt(str));
        }

        int smallest = Collections.min(intSizes);
        area += 2*smallest;

        intSizes.remove(Integer.valueOf(smallest));

        smallest = Collections.min(intSizes);
        area += 2*smallest;
        area += Integer.parseInt(sizes[0]) * Integer.parseInt(sizes[1]) * Integer.parseInt(sizes[2]);

        return area;
    }

    public static void part1() {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath))) {

            int paper = 0;
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                String[] sizes = line.split("x");

                paper += surfaceArea(Integer.parseInt(sizes[0]), Integer.parseInt(sizes[1]), Integer.parseInt(sizes[2]));
            }

            System.out.println(paper);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void part2() {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath))) {

            int paper = 0;
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                String[] sizes = line.split("x");

                paper += ribbon(sizes);
            }

            System.out.println(paper);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        part1();
        part2();
    }
    
}