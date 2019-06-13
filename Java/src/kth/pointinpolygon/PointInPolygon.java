/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */

package kth.pointinpolygon;

import java.util.List;
import java.util.concurrent.ThreadLocalRandom;


public class PointInPolygon 
{	
	/*
	 * Determines if a point is on a segment formed by other two points.
	 * @param s1 The start of the segment.
	 * @param s2 The end of the segment.
	 * @param point The analyzed point.
	 * @return boolean whether the point is on the segment or not.
	 */
	private static boolean pointInSegment(Point s1, Point s2, Point point)
	{
		return s1.dist(s2) == point.dist(s1) + point.dist(s2);	
	}
	
	/*
	 * Iterates over every edge in a given polygon and checks if a given point is
	 * laying on any of them.
	 * @param list_vertices The list of vertices of the polygon.
	 * @param point The analyzed point.
	 * @return boolean whether it lays on a polygon edge or not.
	 */
	private static boolean checkIfIsEdge(List<Point> list_vertices, Point point)
	{
		for (int i = 0; i < list_vertices.size() - 1; i++)
		{
			if (pointInSegment(list_vertices.get(i), list_vertices.get(i+1), point))
			{
				return true;
			}
		}
		return false;
	}
	
	/*
	 * Generates a random number between 100000000 and 300000000.
	 * @return int said random number.
	 */
	private static int random()
	{
		return ThreadLocalRandom.current().nextInt(100000000, 300000000);
	}
	
	/*
	 * Casts a ray from the given point in a random direction and counts how many times 
	 * it intersects with the edges of a polygon, given by its list of vertices.
	 * @param list_vertices The list of vertices of the polygon.
	 * @param point The analyzed point.
	 * @return int 0 or 1, the amount of intersections modulo 2.
	 */
	private static int rayCast(List<Point> list_vertices, Point point)
	{
		int cnt = 0;
		LineSegment ray = new LineSegment(point, new Point(point.x + random(), point.y + random()));
		for (int i = 0; i < list_vertices.size() - 1; i++)
		{
			LineSegment edge = new LineSegment(list_vertices.get(i), list_vertices.get(i+1));
			if (ray.intersection(edge) instanceof LineSegment.SingleIntersection)
			{
				cnt += 1;
			}
		}
		return cnt % 2;
	}
	
	/*
	 * Main method. Determines if a given point is inside, on or outside a polygon formed by
	 * a given list of points. 
	 * @param list_vertices The list of vertices of the polygon.
	 * @param point The analyzed point.
	 * @return String "in", "on" or "out" if the point is inside, on an edge or outside the 
	 * polygon, respectively.
	 */
	public static String solve(List<Point> list_vertices, Point point)
	{
		if (checkIfIsEdge(list_vertices, point))
		{
			return "on";
		}
		else
		{
			// If the amount of intersections ray-polygon is even, the point is outside.
			// Otherwise, it is inside. Check documentation for rayCast() for more info.
			return (rayCast(list_vertices, point) == 0) ? "out" : "in";
		}
	}
}
