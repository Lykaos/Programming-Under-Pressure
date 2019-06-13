/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */

package kth.linesegmentdistance;


public class Reader 
{
    public static void run(Kattio kattio)
    {
        final int n_cases = kattio.getInt();
        for (int i = 0; i < n_cases; i++)
        {
        	Point s1a = new Point(kattio.getInt(), kattio.getInt());
        	Point s1b = new Point(kattio.getInt(), kattio.getInt());
        	Point s2a = new Point(kattio.getInt(), kattio.getInt());
        	Point s2b = new Point(kattio.getInt(), kattio.getInt());
        	LineSegment s1 = new LineSegment(s1a, s1b);
        	LineSegment s2 = new LineSegment(s2a, s2b);
        	double dist = SegmentDistance.solve(s1, s2);
            System.out.printf("%.2f", dist);
            System.out.println();
        }
        kattio.close();
    }

    public static void main(String[] args) 
    {
        run(new Kattio());
    }
}