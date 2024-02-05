import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Day13 {

    static class Happiness {
        String person;
        HashMap<String, Integer> scores = new HashMap<>();

        public Happiness(String person) {
            this.person = person;
        }

        public void addScore(String person, int score) {
            this.scores.put(person, score);
        }

        public int getHappiness(String person) {
            return this.scores.get(person);
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

    static int computeHappiness(List<String> persons, int k, HashMap<String, Happiness> graph, int maxHappiness) 
    {
        if (k == persons.size() && checkUnique(persons)) 
        {
            int happiness = 0;
            happiness += graph.get(persons.get(0)).getHappiness(persons.get(k-1));
            happiness += graph.get(persons.get(k-1)).getHappiness(persons.get(0));
            for (int i = 0; i < persons.size()-1; i++) 
            {
                String from = persons.get(i);
                String to = persons.get(i+1);
                happiness += graph.get(from).getHappiness(to);
                happiness += graph.get(to).getHappiness(from);
            }
            return happiness;
        } 
        else 
        {
            for (int i = k; i < persons.size(); i++) 
            {
                String temp = persons.get(k);
                persons.set(k, persons.get(i));
                persons.set(i, temp);
 
                maxHappiness = Math.max(computeHappiness(persons, k+1, graph, maxHappiness), maxHappiness);
 
                temp = persons.get(k);
                persons.set(k, persons.get(i));
                persons.set(i, temp);
            }
        }

        return maxHappiness;
    }

    static HashMap<String, Happiness> addMyself(HashMap<String, Happiness> graph, List<String> persons) {
        graph.put("Mike", new Happiness("Mike"));
        for (String person : persons) {
            graph.get("Mike").addScore(person, 0);
            graph.get(person).addScore("Mike", 0);
        }

        return graph;
    }
    
    public static void main(String[] args) {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            List<String> persons = new ArrayList<>();
            HashMap<String, Happiness> graph = new HashMap<>();
            while ((line = bufferedReader.readLine()) != null) {
                String[] split = line.split(" ");

                String person = split[0];
                String friend = split[10].replace(".", "");
                int score = Integer.parseInt(split[3]);

                if (!graph.containsKey(person)) {
                    graph.put(person, new Happiness(person));
                    persons.add(person);
                }

                if (line.contains("lose")) 
                    score *= -1;
                
                graph.get(person).addScore(friend, score);
            }

            // part 2
            graph = addMyself(graph, persons);
            persons.add("Mike");
            //

            int maxHappiness = 0;
            maxHappiness = computeHappiness(persons, 0, graph, maxHappiness);
            System.out.println(maxHappiness);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}