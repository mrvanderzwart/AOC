import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Day11 {

    static String generateNextPasswd(String passwd) {
        StringBuilder newPasswd = new StringBuilder(passwd);
        int i = passwd.length()-1;
        while (passwd.charAt(i) == 'z') i--;
        newPasswd.setCharAt(i, (char)(passwd.charAt(i) + 1));
        for (int j = i+1; j < passwd.length(); j++) newPasswd.setCharAt(j, 'a');
        
        return newPasswd.toString();
    }

    static boolean checkFirst(String passwd) {
        for (int i = 0; i < passwd.length()-2; i++) {
            if ((int)passwd.charAt(i) == (int)passwd.charAt(i+1)-1 &&
                (int)passwd.charAt(i) == (int)passwd.charAt(i+2)-2)
                return true;
        }

        return false;
    }

    static boolean checkSecond(String passwd) {
        if (passwd.contains("i") || passwd.contains("o") || passwd.contains("u"))
            return false;

        return true;
    }

    static boolean checkThird(String passwd) {
        char pair = ' ';
        int count = 0;
        for (int i = 0; i < passwd.length()-1; i++) {
            if (passwd.charAt(i) == passwd.charAt(i+1) && passwd.charAt(i) != pair) {
                pair = passwd.charAt(i);
                count++;
                if (count >= 2) 
                    return true;
            }
        }

        return false;
    }

    static boolean validPasswd(String passwd) {
        return (checkFirst(passwd) && checkSecond(passwd) && checkThird(passwd));
    }    
    
    public static void main(String[] args) {
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader("input.txt"))) {
            String passwd = bufferedReader.readLine();
            while (!validPasswd(passwd)) passwd = generateNextPasswd(passwd);
            System.out.println(passwd);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}