/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */

package kth.convexhull;

/* Just a simple 2D point class. It admits points with integer
 * coordinates (x, y) lower than 10^9.
 */
public class Point implements Comparable<Point>
{
	static final int MAX_COORD = 1000000000;
	public final int x; 
	public final int y; 
	
	public Point(int x, int y) 
	{
		this.x = x; 
		this.y = y; 
	}
	
	@Override
	public boolean equals(Object o)
	{
		final Point p = (Point) o;
		return this.x == p.x && this.y == p.y;
	}
	
	@Override
	public String toString()
	{
		return this.x + " " + this.y;
	}
	
	@Override
	public int hashCode() 
	{
	    return this.x * MAX_COORD + this.y;        
	}
	
	public int compareTo(Point p) 
	{
		return (this.x == p.x) ? this.y - p.y : this.x - p.x;
	}
}