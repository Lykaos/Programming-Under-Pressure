package kth.Homework;

import kth.Kattio;

public class Reader {

    public static void run(Kattio kattio) 
    {
        final Homework hw = new Homework(kattio.getWord(), kattio.getWord(), kattio.getWord());
        kattio.println(hw.solve());
        kattio.close();
    }

    public static void main(String[] args) 
    {
        run(new Kattio());
    }
}