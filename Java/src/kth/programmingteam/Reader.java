/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Homework
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 */
package kth.programmingteam;

import kth.Kattio;

import java.util.Map;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Reader 
{
    public static void run(Kattio kattio)
    {
    	while (kattio.hasMoreTokens())
    	{
    		int n = kattio.getInt();
    		Map<String, List<String>> dic = new HashMap<String, List<String>>();
    		for (int i = 0; i < n; i++)
    		{
        		String p1 = kattio.getWord(); String p2 = kattio.getWord();
        		if (dic.get(p1) == null)
        		{
        			List<String> list = new ArrayList<String>();
        			list.add(p2);
        			dic.put(p1, list);
        		}
        		else
        		{
        			dic.get(p1).add(p2);
        		}
        		if (dic.get(p2) == null)
        		{
        			List<String> list = new ArrayList<String>();
        			list.add(p1);
        			dic.put(p2, list);
        		}
        		else
        		{
        			dic.get(p2).add(p1);
        		}
    		}
    		System.out.println(solve(dic));
    	}
        kattio.close();    
    }

    public static String solve(Map<String, List<String>> dic)
    {
    	if (dic.size() == 0)
    	{
    		return "possible";
    	}
    	String min_idx = "";
    	int mini = Integer.MAX_VALUE;
    	for (String k : dic.keySet())
    	{
    		int size = dic.get(k).size();
    		if (size < 2)
    		{
    			return "impossible";
    		}
    		else if (size < mini)
    		{
    			min_idx = k;
    		}
    	}
    	
    	/*
        if len(dic) == 0:
            return "possible"
        min_idx = min(dic.items(), key=lambda x: len(x[1]))[0]
        if len(dic[min_idx]) < 2:
            return "impossible"
        ways = combinations(dic[min_idx], 2)
        for w in ways:
            new_dic = dict(dic)
            for j in [min_idx, w[0], w[1]]:
                del new_dic[j]
                for k in new_dic.values():
                    if j in k:
                        k.remove(j)
            if solve(new_dic) == "possible":
                return "possible"
                		*/
    	return "impossible";
    }
    public static void main(String[] args) 
    {
        run(new Kattio());
    }
}