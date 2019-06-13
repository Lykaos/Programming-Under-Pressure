/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */

package kth.linesegmentdistance;


public class SegmentDistance 
{	
	/*
	 * Calculates the distance between a point and a segment. It checks
	 * if the projection of the point is on the given segment and 
	 * applies Heron's formula if that is the case. Otherwise, just
	 * calculates the minimum of the distances from the point to the ends
	 * of the segments.
	 * @param p The analyzed point
	 * @param sa The start of the segment
	 * @param sb The end of the segment
	 * @return A double with the minimum distance from the point to the segment
	 */
	private static double distPointToSeg(Point p, Point sa, Point sb)
	{
		double a = p.dist(sa);
		double b = p.dist(sb);
		double c = sa.dist(sb);
		double dotProduct = (p.x - sa.x) * (sb.x - sa.x) + (p.y - sa.y) * (sb.y - sa.y);
		
		if (dotProduct > 0 && dotProduct < Math.pow(c, 2))
		{
			// Heron's formula. The height of the formed triangle will be the
			// distance from the point to the segment.
			double s = (a + b + c) / 2;
			return 2 * Math.sqrt(s * (s-a) * (s-b) * (s-c)) / c;
		}
		else
		{
			return Math.min(a, b);
		}
	}
	
	/*
	 * Calculates the distance between two segments that do not intersect.
	 * Given two segments AB and CD, calculates the minimum of the distances
	 * A-CD, B-CD, C-AB and D-AB.
	 * @param s1 Segment 1
	 * @param s2 Segment 2
	 * @return A double with the minimum distance between the given segments.
	 */
	public static double distSegments(LineSegment s1, LineSegment s2)
	{
		double s1a = distPointToSeg(s1.a, s2.a, s2.b);
		double s1b = distPointToSeg(s1.b, s2.a, s2.b);
		double s2a = distPointToSeg(s2.a, s1.a, s1.b);
		double s2b = distPointToSeg(s2.b, s1.a, s1.b);
		return Math.min(Math.min(s1a, s1b), Math.min(s2a, s2b));
	}
	
	/*
	 * Main method. Determines the minimum distance between two segments,
	 * which will be 0 if they intersect.
	 * @param s1 Segment 1
	 * @param s2 Segment 2
	 * @return A double with the minimum distance between the given segments.
	 */
	public static double solve(LineSegment s1, LineSegment s2)
	{
		LineSegment.Result intersection = s1.intersection(s2);
		if (intersection instanceof LineSegment.NoIntersection)
		{
			return distSegments(s1, s2);
		}
		else
		{
			return 0;
		}
	}
}
