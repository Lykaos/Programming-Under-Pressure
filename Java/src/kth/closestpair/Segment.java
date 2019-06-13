package kth.closestpair;

public class Segment 
{
	Point a;
	Point b;
	
    public Segment(Point a, Point b) 
    {
        this.a = a;
        this.b = b;
    }
    
    public double dist()
    {
    	return this.a.dist(this.b);
    } 
}
