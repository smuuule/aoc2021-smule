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
        objReader = new BufferedReader(new FileReader("C:/Users/samue/Documents/GitHub/aoc2021-smule/2dec/input.txt"));
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

        int x = 0;
        int y = 0;

        for (int i = 0; i < data.size(); i++) {
            String[] in = data.get(i).split(" ");
            String cmd = in[0];
            int val = Integer.parseInt(in[1]);

            if (cmd.equals("forward")) {
                x += val;
            }
            else if (cmd.equals("down")) {
                y += val;
            }
            else if (cmd.equals("up")) {
                y -= val;
            }
        }

        System.out.printf("Coordinates (%d, %d)\n", x, y);
        System.out.printf("Multiplication: %d", x*y);
    }
}