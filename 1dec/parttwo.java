import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class parttwo {
    public static void main(String[] args) {
        BufferedReader objReader = null;
        ArrayList<Integer> data = new ArrayList<Integer>();
        try {
        String strCurrentLine;
        objReader = new BufferedReader(new FileReader("C:/Users/samue/Documents/GitHub/aoc2021-smule/1dec/input.txt"));
        while ((strCurrentLine = objReader.readLine()) != null) {
            data.add(Integer.parseInt(strCurrentLine));
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
        for (int i = 0; i < data.size()-3; i++) {
            if ((data.get(i) + data.get(i+1) + data.get(i+2)) < (data.get(i+1) + data.get(i+2) + data.get(i+3))) {
                count += 1;
            }
        }
        System.out.println("count: " + count);
    }
}