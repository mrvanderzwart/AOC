import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

class Day7 {

    public static String filePath = "input.txt";

    public static Map<String, short> setWire(Map<String,short> wires, String wire1, String wire2, String resultWire, String operation) {
        short result = 0;
        switch (operation) {
            case "AND":
                result = wires.getOrDefault(wire1, 0)&wires.getOrDefault(wire2, 0); 
                break;
            case "OR":
                result = wires.getOrDefault(wire1, 0)|wires.getOrDefault(wire2, 0); 
                break;
            case "LSHIFT":
                result = wires.getOrDefault(wire1, 0)<<Integer.parseInt(wire2); 
                break;
            case "RSHIFT":
                result = wires.getOrDefault(wire1, 0)>>Integer.parseInt(wire2); 
                break;
            case "NOT":
                result = ~wires.getOrDefault(wire1, 0);
            default:
                break;
        }

        wires.put(resultWire, result);

        return wires;
    }

    public static void part1() {
        String line;
        Map<String, short> wires = new HashMap<>();
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath))) {
            while ((line = bufferedReader.readLine()) != null) {
                String[] split = line.split("->");
                String resultWire = split[1];

                split = split[0].split(" ");
                String wire1 = "";
                String wire2 = "";
                String operation = "";
                if (split.length == 3) {
                    System.out.println("IF");
                    System.out.println(split[0]);
                    System.out.println(split[1]);
                    System.out.println(split[2]);
                    wire1 = split[0];
                    wire2 = split[2];
                    operation = split[1];
                } else if (split.length == 2) {
                    System.out.println("ELSE");
                    System.out.println(split[0]);
                    System.out.println(split[1]);
                    wire1 = split[1];
                    operation = split[0];
                } else 
                    try {
                        wires.put(resultWire, Integer.parseInt(split[0]));
                    } catch (NumberFormatException e) {
                        wires.put(resultWire, wires.get(split[0]));
                    }

                wires = setWire(wires, wire1, wire2, resultWire, operation);
            }

            System.out.println(wires);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        part1();
        //part2();
    }
    
}