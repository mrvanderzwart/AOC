import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

class Day17 {

    public static int findCombinations(List<Integer> containers, List<Integer> currentCombination, int target, int nCombinations) {
        System.out.println(currentCombination);
        if (currentCombination.size() != 0 && currentCombination.stream().reduce(0, Integer::sum) == target) {
            System.out.println("erin");
            System.out.println(currentCombination);
            return nCombinations+1;
        }

        for (int container : new ArrayList<>(containers)) {
            List<Integer> newCombination = new ArrayList<>(currentCombination);
            newCombination.add(container);
            containers.remove(Integer.valueOf(container));
            nCombinations = findCombinations(containers, newCombination, target, nCombinations);
            containers.add(container);
        }

        return nCombinations;
    }

    public static void main(String[] args) {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader("input.txt"))) {
            List<Integer> containers = new ArrayList<>();
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                containers.add(Integer.parseInt(line));
            }
            int nCombinations = 0;
            nCombinations = findCombinations(containers, new ArrayList<>(), 25, nCombinations);
            System.out.println(nCombinations);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}