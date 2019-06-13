/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */
package kth.XYZZY;

import kth.Kattio;

import java.util.ArrayList;
import java.util.List;

public class XYZZY 
{
    public static void run(Kattio kattio) 
    {
        while(true) 
        {
            final int n_rooms = kattio.getInt();
            
            if (n_rooms == -1)
            {
            	break;
            }
            
            final List<BellmanFord.Edge> edges = new ArrayList<>();
            int[] weights = new int[n_rooms];
            
            for (int i = 0; i < n_rooms; i++)
            {
            	weights[i] = kattio.getInt(); 
            	int n_doors = kattio.getInt();
            	
            	for (int j = 0; j < n_doors; j++)
            	{
            		edges.add(new BellmanFord.Edge(i, kattio.getInt() - 1, 0));
            	}
            }
            
            for (BellmanFord.Edge e : edges)
            {
            	e.weight = -1*weights[e.v];
            }
            
            final BellmanFord.Solution solution = BellmanFord.shortestPath(n_rooms, edges, 0);
                         
            if (solution.distances[n_rooms - 1] == Integer.MAX_VALUE) 
            {
                System.out.println("hopeless");
            } 
            else 
            {
            	System.out.println("winnable");
            }
        }

        kattio.close();
    }

    public static void main(String[] args) 
    {
        run(new Kattio());
    }
}