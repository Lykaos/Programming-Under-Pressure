package kth.TenKindsOfPeople;

public class TenKindsOfPeople {

	String[] map;
	int rows;
	int cols;
	UnionFind forest;
	
	public TenKindsOfPeople(String[] map, int rows, int cols)
	{
		this.map = map;
		this.rows = rows;
		this.cols = cols;
        this.forest = new UnionFind(rows*cols);
        for (int i = 0; i < rows; i++)
        {
        	for (int j = 0; j < cols; j++)
        	{
        		int term1 = i*cols + j;
        		if (j < cols - 1 && map[i].charAt(j) == map[i].charAt(j+1))
        		{
        			forest.union(term1, i*cols + j+1);
        		}
        		if (i < rows - 1 && map[i].charAt(j) == map[i+1].charAt(j))
        		{
        			forest.union(term1, (i+1)*cols + j);
        		}
        	}
        }
	}
	
	public String solve(int r1, int c1, int r2, int c2)
	{
		if (forest.same(r1*cols + c1, r2*cols + c2))
		{
			return map[r1].charAt(c1) == '1' ? "decimal" : "binary";
		}
        return "neither";
	}
}