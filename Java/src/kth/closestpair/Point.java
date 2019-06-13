package kth.closestpair;

class Point implements Comparable<Point>
{
    static final int MAX_COORD = 1000000000;
    public double x; 
    public double y; 
    
    public Point(double x, double y) 
    {
        this.x = x; 
        this.y = y; 
    }
    
	public double dist(Point p)
	{
		return Math.pow(this.x - p.x, 2) + Math.pow(this.y - p.y, 2);
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
        return (this.x > p.x) ? 1 : (this.x == p.x) ? 0 : -1; 
    }
}
