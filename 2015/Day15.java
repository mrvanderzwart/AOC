import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Day15 {

    static class Property {

        int capacity;
        int durability;
        int flavor;
        int texture;
        int calories;

        public void setProperty(String property, int amount) {
            switch (property) {
                case "capacity":
                    this.capacity = amount;
                    break;
                case "durability":
                    this.durability = amount;
                    break;
                case "flavor":
                    this.flavor = amount;
                    break;
                case "texture":
                    this.texture = amount;
                    break;
                case "calories":
                    this.calories = amount;
                    break;
                default:
                    break;
            }
        }

        public int getProperty(String property) {
            switch (property) {
                case "capacity":
                    return this.capacity;
                case "durability":
                    return this.durability;
                case "flavor":
                    return this.flavor;
                case "texture":
                    return this.texture;
                case "calories":
                    return this.calories;
                default:
                    return this.capacity;
            }
        }
    }

    public static int findBestCookie(int targetSum, int nNumbers, List<Integer> currentCombination, int maximum, HashMap<String, Property> properties, List<String> propertyList, List<String> ingredientList) {
        if (nNumbers == 0) {
            if (currentCombination.stream().mapToInt(Integer::intValue).sum() == targetSum) {
                int totalSum = 0;
                boolean first = true;
                for (String property : propertyList) {
                    int propertySum = 0;
                    for (int i = 0; i < currentCombination.size(); i++) {
                        propertySum += (currentCombination.get(i) * properties.get(ingredientList.get(i)).getProperty(property));
                    }

                    if (property == "calories") { 
                        if (propertySum != 500) // part 2
                            return maximum; 

                        continue;
                    }

                    if (propertySum < 0) propertySum = 0;

                    if (first) {
                        totalSum = propertySum;
                        first = false;
                    }
                    else totalSum *= propertySum;
                }

                maximum = Math.max(totalSum, maximum);
            }
            return maximum;
        }

        for (int num = 0; num <= targetSum; num++) {
            List<Integer> newCombination = new ArrayList<>(currentCombination);
            newCombination.add(num);
            maximum = findBestCookie(targetSum, nNumbers-1, newCombination, maximum, properties, propertyList, ingredientList);
        }

        return maximum;
    }

    public static HashMap<String, Property> addProperties(String[] split, String ingredient, HashMap<String, Property> properties) {
        properties.put(ingredient, new Property());

        properties.get(ingredient).setProperty("capacity", Integer.parseInt(split[2].replace(",", "")));
        properties.get(ingredient).setProperty("durability", Integer.parseInt(split[4].replace(",", "")));
        properties.get(ingredient).setProperty("flavor", Integer.parseInt(split[6].replace(",", "")));
        properties.get(ingredient).setProperty("texture", Integer.parseInt(split[8].replace(",", "")));
        properties.get(ingredient).setProperty("calories", Integer.parseInt(split[10]));

        return properties;
    }

    public static void main(String[] args) {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            List<String> propertyList = new ArrayList<>() {
                {
                    add("capacity");
                    add("durability");
                    add("flavor");
                    add("texture");
                    add("calories");
                }
            };
            List<String> ingredientList = new ArrayList<>();
            HashMap<String, Property> properties = new HashMap<>();
            int nNumbers = 0;
            while ((line = bufferedReader.readLine()) != null) {
                nNumbers++;
                String[] split = line.split(" ");
                String ingredient = split[0].replace(":", "");
                ingredientList.add(ingredient);
                properties = addProperties(split, ingredient, properties);
            }
            int maximum = 0;
            maximum = findBestCookie(100, nNumbers, new ArrayList<>(), maximum, properties, propertyList, ingredientList);
            System.out.println(maximum);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}