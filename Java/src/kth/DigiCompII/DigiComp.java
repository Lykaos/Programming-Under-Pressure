package kth.DigiCompII;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import kth.Kattio;

public class DigiComp {

	public static List<Integer> queue = new ArrayList<Integer>();
	
    public static void run(Kattio kattio) {

        final long n_balls = kattio.getLong();
        final int n_switches = kattio.getInt();
        long[] balls = new long[n_switches + 1];
        Arrays.fill(balls,  0);
        balls[1] = n_balls;
        int[][] switches = new int[n_switches + 1][3];
        int[] appearances = new int[n_switches + 1];
        Arrays.fill(appearances,  0);
        
        for (int i = 1; i < n_switches + 1; i++)
        {
        	switches[i][0] = getPos(kattio.getWord());
        	switches[i][1] = kattio.getInt(); 
        	switches[i][2] = kattio.getInt();
        	appearances[switches[i][1]] += 1;
        	appearances[switches[i][2]] += 1;
        }

        topologicalSort(queue, appearances, n_switches, switches);
        
        for (int j = 0; j < queue.size(); j++)
        {
        	int i = queue.get(j);
        	int[] sw = switches[i];
        	int L_node = sw[1];
        	int R_node = sw[2];
        	long ceil = 0;
        	long floor = 0;
        	
        	if (balls[i] % 2 == 0)
        	{
        		ceil = balls[i] / 2;
        		floor = balls[i] / 2;
        	}
        	else
        	{
        		ceil = (balls[i] + 1) / 2;
        		floor = (balls[i] - 1) / 2;
        	}
        	
        	if (sw[0] == 0)
        	{
        		balls[L_node] += ceil;
        		balls[R_node] += floor;
        	}
        	else
        	{
        		balls[R_node] += ceil;
        		balls[L_node] += floor;
        	}
        }
        for (int i = 1; i < n_switches + 1; i++)
        {
        	if (balls[i] % 2 == 0)
        	{
        		kattio.print(getDirection(switches[i][0]));
        	}
        	else
        	{
        		kattio.print(changePos(getDirection(switches[i][0])));
        	}
        }
        kattio.close();
    }

    public static void main(String[] args) 
    {
        run(new Kattio());
    }
    
    private static int getPos(String pos)
    {
    	return (pos.equals("R")) ? 1 : 0;
    }
    
    private static String getDirection(int pos)
    {
    	return (pos == 1) ? "R" : "L";
    }
    
    private static String changePos(String pos)
    {
    	return (pos.equals("L")) ? "R" : "L";
    }
    
    private static void topologicalSort(List<Integer> queue, int[] appearances, int n_switches, int[][] switches)
    {
    	for (int i = 2; i < n_switches; i++)
    	{
    		if (appearances[i] == 0)
    		{
    			queue.add(i);
    		}
    	}
    	int current = 0;
    	queue.add(1);
    	
    	while (queue.size() < n_switches)
    	{
    		int sleft = switches[queue.get(current)][1];
    		int sright = switches[queue.get(current)][2];
    		
    		if (sleft == 0 && sright == 0)
    		{
    			current += 1;
    			continue;
    		}
    		if (sleft == sright)
    		{
    			appearances[sleft] -= 2;
    			if (appearances[sleft] == 0)
    			{
    				queue.add(sleft);
    			}
    			current += 1;
    		}
    		else
    		{
    			appearances[sleft] -= 1;
    			if (appearances[sleft] == 0)
    			{
    				queue.add(sleft);
    			}            
                appearances[sright] -= 1;
                if (appearances[sright] == 0)
                {
                	queue.add(sright);
                }
                current += 1;
    		}
    	}  
    }
}

