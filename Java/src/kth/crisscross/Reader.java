package kth.crisscross;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Reader 
{
	public static int solve(List<LineSegment> list)
	{
		Set<Point> set_points = new HashSet<Point>();
		for (int i = 0; i < list.size(); i++)
		{
			LineSegment l1 = list.get(i);
			for (int j = i + 1; j < list.size(); j++)
			{
				LineSegment l2 = list.get(j);
				LineSegment.Result res = l1.intersection(l2);
				if (res instanceof LineSegment.InfiniteIntersection)
				{
					return -1;
				}
				else if (res instanceof LineSegment.SingleIntersection)
				{
					final LineSegment.SingleIntersection single = (LineSegment.SingleIntersection) res;
					set_points.add(new Point(single.cx, single.cy, single.cz));
				}
			}
		}
		return set_points.size();
	}
	
    public static void run(Kattio kattio)
    {
    	final int n = kattio.getInt();
    	List<LineSegment> list_segments = new ArrayList<LineSegment>();
	    for (int i = 0; i < n; i++)
	    {
	    	//Point p1 = new Point(kattio.getInt(), kattio.getInt());
	    	//Point p2 = new Point(kattio.getInt(), kattio.getInt());
	    	//list_segments.add(new LineSegment(p1, p2));
	    }
    	System.out.println(solve(list_segments));
        kattio.close();
    }

    public static void main(String[] args) 
    {
        run(new Kattio());
    }
}