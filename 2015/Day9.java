import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Day9 {

    static class Distances {
        String start;
        HashMap<String, Integer> destinations = new HashMap<>();

        public Distances(String start) {
            this.start = start;
        }

        public void addDestination(String destination, int distance) {
            this.destinations.put(destination, distance);
        }

        public int getCost(String destination) {
            return this.destinations.get(destination);
        }
    }

    static boolean checkUnique(List<String> cities) {
        List<String> copy = new ArrayList<>();

        for (String city : cities) {
            if (copy.contains(city))
                return false;

            copy.add(city);
        }

        return true;
    }

    static int computeCost(List<String> cities, int k, HashMap<String, Distances> graph, int maxCost) 
    {
        if (k == cities.size() && checkUnique(cities)) 
        {
            int cost = 0;
            for (int i = 0; i < cities.size()-1; i++) 
            {
                String from = cities.get(i);
                String to = cities.get(i+1);
                cost += graph.get(from).getCost(to);
            }
            return cost;
        } 
        else 
        {
            for (int i = k; i < cities.size(); i++) 
            {
                String temp = cities.get(k);
                cities.set(k, cities.get(i));
                cities.set(i, temp);
 
                maxCost = Math.max(computeCost(cities, k + 1, graph, maxCost), maxCost);
 
                temp = cities.get(k);
                cities.set(k, cities.get(i));
                cities.set(i, temp);
            }
        }

        return maxCost;
    }
    
    public static void main(String[] args) {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            List<String> cities = new ArrayList<>();
            HashMap<String, Distances> graph = new HashMap<>();
            while ((line = bufferedReader.readLine()) != null) {
                String[] split = line.split(" ");

                String from = split[0];
                String to = split[2];
                int distance = Integer.parseInt(split[4]); 

                if (!graph.containsKey(from)) {
                    graph.put(from, new Distances(from));
                    cities.add(from);
                }
                graph.get(from).addDestination(to, distance);

                if (!graph.containsKey(to)) {
                    graph.put(to, new Distances(to));
                    cities.add(to);
                }
                graph.get(to).addDestination(from, distance);
            }

            int maxCost = 0;
            maxCost = computeCost(cities, 0, graph, maxCost);
            System.out.println(maxCost);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}