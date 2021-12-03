import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class partone {
    public static void main(String[] args) {
        BufferedReader objReader = null;
        ArrayList<String> data = new ArrayList<String>();

        try {
        String strCurrentLine;
        objReader = new BufferedReader(new FileReader("C:/Users/samue/Documents/GitHub/aoc2021-smule/1dec/input.txt"));
        while ((strCurrentLine = objReader.readLine()) != null) {
            data.add(strCurrentLine);
        }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {

        try {
            if (objReader != null)
            objReader.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        }

        int count = 0;
        for (int i = 0; i < data.size()-1; i++) {
            if (Integer.parseInt(data.get(i)) < Integer.parseInt(data.get(i+1))) {
                count += 1;
            }
        }
        System.out.println("count: " + count);
    }
}