package kth.herkabe;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Reader 
{
    public static void run(Kattio kattio)
    {
    	final int n = kattio.getInt();
    	List<String> w = new ArrayList<String>();
	    for (int i = 0; i < n; i++)
	    {
	    	w.add(kattio.getWord());
	    }
    	Collections.sort(w);
    	Solver solver = new Solver(w);
    	System.out.println(solver.solve(0, w.size(), 0));
        kattio.close();
    }

    public static void main(String[] args) 
    {
        run(new Kattio());
    }
}