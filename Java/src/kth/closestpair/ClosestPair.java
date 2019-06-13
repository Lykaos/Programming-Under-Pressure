/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */

package kth.closestpair;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ClosestPair 
{   
	// Brute force method for calculating the closest pair in a very
	// small set of points.
    private static Segment bruteForce(List<Point> list_points)
    {
    	int size = list_points.size();
        double min = Double.MAX_VALUE;
        Point min1 = null;
        Point min2 = null;
        for (int i = 0; i < size; i++)  
        {
            Point p1 = list_points.get(i);
            for (int j = i+1; j < size; j++)    
            {
                Point p2 = list_points.get(j);
                double dist = p1.dist(p2);
                if (dist < min)
                {
                    min = dist;
                    min1 = p1;
                    min2 = p2;       
                }
            }
        }
        return new Segment(min1, min2); 
    }
    
    // Generates a sorted list of points by merge sorting two sorted lists of points 
    // (sorted by y coordinate).
    public static List<Point> mergeSort(List<Point> l, List<Point> r)
    {
        int i = 0;
        int j = 0;
        List<Point> res = new ArrayList<Point>();
        while (i < l.size() && j < r.size())
        {
            Point left = l.get(i);
            Point right = r.get(j);
            if (left.y < right.y)
            {
                res.add(left);
                i++;
            }
            else
            {
                res.add(right);
                j++;
            }
        }
        if (j < r.size())
        {
            res.addAll(r.subList(j, r.size()));
        }
        if (i < l.size())
        {
            res.addAll(l.subList(i, l.size()));
        }
        
        return res;
    }
    
    // Recursive divide and conquer algorithm
    public static Pair findClosest(List<Point> list_points)
    {
    	int size = list_points.size();
    	// If the partition is small enough, brute force the closest pair.
        if (size < 4)
        {
        	Collections.sort(list_points, (a, b) -> a.y < b.y ? -1 : a.y == b.y ? 0 : 1);
            return new Pair(bruteForce(list_points), list_points);
        }
        
        // Otherwise, divide more.
        int mid = size / 2;
        Point p_mid = list_points.get(mid);
        Pair d1 = findClosest(list_points.subList(0,  mid));
        Pair d2 = findClosest(list_points.subList(mid, size));
        
        // This is the closest pair in the divided sets, but we haven't 
        // checked the points in the middle area yet.
        Segment d = (d1.s.dist() <= d2.s.dist()) ? d1.s : d2.s;
        double d_dist = d.dist();
        
        // This makes the algorithm nlogn, by returning the sorted points
        // we can just merge sort both sides in n time.
        List<Point> mergesort = mergeSort(d1.l, d2.l);
        
        // Remove all the points that are further than d from the dividing 
        // line, since we already checked those.
        List<Point> between = new ArrayList<Point>();
        for (int i = 0; i < mergesort.size(); i++) 
        {
            Point p = mergesort.get(i);
            if (Math.abs(p.x - p_mid.x) < d_dist)
            {
                between.add(p);
            }
        }

        // Brute force for the points close to the dividing line. 
        // Theorem: second for only runs 6 times at most.
        for (int i = 0; i < between.size(); i++)
        {
            Point p1 = between.get(i);
            for (int j = i+1; j < Math.min(between.size(), i+6); j++)
            {
                Point p2 = between.get(j);
                if (p1.y - p2.y >= d_dist)
                {
                    break;
                }
                double b_dist = p1.dist(p2);
                if (b_dist < d_dist)
                {
                    d_dist = b_dist;
                    d.a = p1;
                    d.b = p2;
                }
            }
        }
        return new Pair(d, mergesort);
    }
    
    public static Segment solve(List<Point> list_points)
    {
        Collections.sort(list_points); // Sort the points by x coord.
        return findClosest(list_points).s;
    }
}