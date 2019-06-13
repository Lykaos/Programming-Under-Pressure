/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */

package kth.pointinpolygon;

import java.util.List;
import java.util.ArrayList;

public class Reader 
{
    public static void run(Kattio kattio)
    {
    	while (kattio.hasMoreTokens())
    	{
	        final int n_vertices = kattio.getInt();
	        if (n_vertices == 0)
	        {
	        	break;
	        }
	        List<Point> list_vertices = new ArrayList<Point>();
	        for (int i = 0; i < n_vertices; i++)
	        {
	        	list_vertices.add(new Point(kattio.getInt(), kattio.getInt()));
	        }
			list_vertices.add(list_vertices.get(0)); // Last edge
	        final int n_points = kattio.getInt();
	        for (int i = 0; i < n_points; i++)
	        {
	        	Point point = new Point(kattio.getInt(), kattio.getInt());
	        	System.out.println(PointInPolygon.solve(list_vertices, point));
	        }
    	}
        kattio.close();
    }

    public static void main(String[] args) 
    {
        run(new Kattio());
    }
}