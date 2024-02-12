import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;

class Day16 {

    static boolean isSue(String[] split, HashMap<String, Integer> tape) {
        for (int i = 2; i < split.length; i += 2) {
            String compound = split[i].replace(":", "");
            Integer amount = Integer.parseInt(split[i+1].replace(",", ""));

            if ((compound.equals("cats") || compound.equals("trees")) && amount <= tape.get(compound))
                return false;
            else if ((compound.equals("pomeranians") || compound.equals("goldfish")) && amount >= tape.get(compound))
                return false;
            else if (!(compound.equals("cats") || compound.equals("trees")) && !(compound.equals("pomeranians") || compound.equals("goldfish")) && tape.get(compound) != amount)
                return false;
        }

        return true;
    }

    public static void main(String[] args) {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader("input.txt"))) {
            HashMap<String, Integer> tape = new HashMap<>() {
                {
                    put("children", 3);
                    put("cats", 7);
                    put("samoyeds", 2);
                    put("pomeranians", 3);
                    put("akitas", 0);
                    put("vizslas", 0);
                    put("goldfish", 5);
                    put("trees", 3);
                    put("cars", 2);
                    put("perfumes", 1);
                }
            };
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                String[] split = line.split(" ");
                int sue = Integer.parseInt(split[1].replace(":", ""));

                if (isSue(split, tape)) {
                    System.out.println(sue);
                    break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}