/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */
package kth.TenKindsOfPeople;

import kth.Kattio;

public class Reader 
{
    public static void run(Kattio kattio)
    {
        final int rows = kattio.getInt(), cols = kattio.getInt();
        final String[] map = new String[rows];      
        for (int i = 0; i < rows; i++)
        {
        	map[i] = kattio.getWord();
        }
    	TenKindsOfPeople people = new TenKindsOfPeople(map, rows, cols);
        final int n = kattio.getInt();
        for (int i = 0; i < n; i++)
        {
        	System.out.println(people.solve(kattio.getInt()-1, kattio.getInt()-1, kattio.getInt()-1, kattio.getInt()-1));
        }
        kattio.close();
    }

    public static void main(String[] args) 
    {
        run(new Kattio());
    }
}