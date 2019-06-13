/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */

package kth.convexhull;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class ConvexHull 
{
	/*
	 * Checks if the sequence of points p1-p2 with p3 are in counter-clockwise order
	 * (the slope of the segment p1-p2 is lower than the slope of the segment p2-p3).
	 * @param p1, p2, p3 The sequence of points
	 * @return true if the sequence is in counter-clockwise order, otherwise false
	 */
	private static boolean isCCW(Point p1, Point p2, Point p3)
	{
		return  (p2.y - p1.y) * (p3.x - p2.x) < (p2.x - p1.x) * (p3.y - p2.y);
	}
	
	/*
	 * Gets the sequence of points that form a partial convex hull on a given list of 
	 * points:
	 * - Lower hull if the list of all the coordinates is sorted in ascending order.
	 * - Upper hull if the list of all the coordinates is sorted in descending order.
	 * @param sorted_points A list with all the points sorted as indicated above
	 * @return The list of points that form the partial hull
	 */
	private static List<Point> getHull(List<Point> sorted_points)
	{
		List<Point> hull = new ArrayList<Point>();
		
		for (Point p : sorted_points)
		{
			int size = hull.size();
			while (size > 1 && !isCCW(hull.get(size - 2), hull.get(size - 1), p))
			{
				// Removes the last element of the hull every time the last two points 
				// of the hull and the current point do not make a counter-clockwise turn.
				hull.remove((size--) - 1);
			}
			hull.add(p);
		}
		
		// Since the last element of any partial hull is the start of the other, it 
		// is necessary to remove it at the end.
		hull.remove(hull.size() - 1);
		return hull;
	}
	
	/* 
	 * Main method. Returns the convex hull that surrounds a given list of points.
	 * @param list_points The list of all the points in the plane
	 * @return A list with the points that form the convex hull
	 */
	public static List<Point> solve(List<Point> list_points)
	{
		// The convex hull of 1 or 2 points is themselves.
		if (list_points.size() < 3)
		{
			return list_points;
		}
		
		Collections.sort(list_points);
		List<Point> lower_hull = getHull(list_points);
		Collections.reverse(list_points);
		List<Point> upper_hull = getHull(list_points);
		
		// Concatenates both partial hulls.
		lower_hull.addAll(upper_hull);
		return lower_hull;
	}
}
