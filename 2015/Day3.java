import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

class House {
    private int x;
    private int y;

    public House(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return this.x;
    }

    public int getY() {
        return this.y;
    }
}

class Day3 {

    public static String filePath = "input.txt";

    public static boolean checkSeen(List<House> houseList, House newHouse) {
        for (House house : houseList) {
            if (house.getX() == newHouse.getX() && 
                house.getY() == newHouse.getY()) 
                return true;
        }

        return false;
    }

    public static List<Integer> movePosition(int x, int y, char character) {
        List<Integer> newPositions = new ArrayList<>();
        switch (character) {
            case '^':
                y--;
                break;
            case 'v':
                y++;
                break;
            case '<':
                x--;
                break;
            case '>':
                x++;
                break;
            default:
                break;
        }

        newPositions.add(x);
        newPositions.add(y);

        return newPositions;
    }

    public static void part1() {
        try (FileReader fileReader = new FileReader(filePath);
            BufferedReader bufferedReader = new BufferedReader(fileReader)) {

            List<House> houseList = new ArrayList<>();

            int x = 0;
            int y = 0;

            int charCode;
            while ((charCode = bufferedReader.read()) != -1) {
                char character = (char) charCode;

                House house = new House(x, y);
                if (!checkSeen(houseList, house))
                    houseList.add(house);

                List<Integer> newPositions = new ArrayList<>();
                newPositions = movePosition(x, y, character);
                x = newPositions.get(0);
                y = newPositions.get(1);
            }

            System.out.println(houseList.size());

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void part2() {
        try (FileReader fileReader = new FileReader(filePath);
            BufferedReader bufferedReader = new BufferedReader(fileReader)) {

            List<House> houseList = new ArrayList<>() {
                {
                    add(new House(0, 0));
                }
            };

            ArrayList<Integer> positions = new ArrayList<>() {
                {
                    add(0);
                    add(0);
                    add(0);
                    add(0);
                }
            };

            int xIndex;
            int yIndex;
            boolean turn = true;

            int charCode;
            while ((charCode = bufferedReader.read()) != -1) {
                char character = (char) charCode;

                if (turn) {
                    xIndex = 0;
                    yIndex = 1;
                } else {
                    xIndex = 2;
                    yIndex = 3;
                }

                List<Integer> newPositions = new ArrayList<>();
                newPositions = movePosition(positions.get(xIndex), positions.get(yIndex), character);
                positions.set(xIndex, newPositions.get(0));
                positions.set(yIndex, newPositions.get(1));

                House house = new House(positions.get(xIndex), positions.get(yIndex));
                if (!checkSeen(houseList, house))
                    houseList.add(house);

                turn = !turn;
            }

            System.out.println(houseList.size());

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        part1();
        part2();
    }
    
}