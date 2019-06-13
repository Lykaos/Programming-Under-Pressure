/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */

package kth.closestpair;

import java.util.ArrayList;
import java.util.List;

public class Reader 
{
    public static void run(Kattio kattio)
    {
    	long startTime = System.currentTimeMillis();

    	while (kattio.hasMoreTokens())
    	{
	        final int n_points = kattio.getInt();
	        if (n_points == 0)
	        {
	        	break;
	        }
	        List<Point> list_points = new ArrayList<Point>();
	        for (int i = 0; i < n_points; i++)
	        {
	        	list_points.add(new Point(kattio.getDouble(), kattio.getDouble()));
	        }
        	Segment closest_pair = ClosestPair.solve(list_points);
            System.out.println(closest_pair.a + " " + closest_pair.b);
    	}
    	
        long stopTime = System.currentTimeMillis();
        long elapsedTime = stopTime - startTime;
        System.out.println("Total time: " + elapsedTime);
        
        kattio.close();
    }

    public static void main(String[] args) 
    {
        run(new Kattio());
    }
}