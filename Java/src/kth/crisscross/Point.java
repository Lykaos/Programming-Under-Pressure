/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */

package kth.crisscross;

/* Just a simple 2D point class. It admits points with integer
 * coordinates (x, y) lower than 10^9.
 */
public class Point implements Comparable<Point>
{
	static final int MAX_COORD = 1000000000;
	public final long x; 
	public final long y; 
	public final long z;
	
	public Point(long x2, long y2, long z) 
	{
		this.x = x2; 
		this.y = y2; 
		this.z = z;
	}
	
	public double dist(Point p)
	{
		return Math.sqrt(Math.pow(this.x - p.x, 2) + Math.pow(this.y - p.y, 2));
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
	    return (int) (this.x * MAX_COORD + this.y);        
	}
	
	public int compareTo(Point p) 
	{
		return (int) ((this.x == p.x) ? this.y - p.y : this.x - p.x);
	}
}