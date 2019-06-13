/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */

package kth.convexhull;

import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

public class Reader 
{
    public static void run(Kattio kattio)
    {
    	while (kattio.hasMoreTokens())
    	{
	        final int n_points = kattio.getInt();
	        if (n_points == 0)
	        {
	        	break;
	        }
	        Set<Point> set_points = new HashSet<Point>();
	        for (int i = 0; i < n_points; i++)
	        {
	        	set_points.add(new Point(kattio.getInt(), kattio.getInt()));
	        }
	        
	        List<Point> convex_hull = ConvexHull.solve(new ArrayList<Point>(set_points));
	        
	        kattio.println(convex_hull.size());
	        for (Point p : convex_hull)
	        {
	        	kattio.println(p.x + " " + p.y);
	        }
    	}
        kattio.close();
    }

    public static void main(String[] args) 
    {
        run(new Kattio());
    }
}