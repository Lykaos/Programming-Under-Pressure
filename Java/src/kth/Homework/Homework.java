package kth.Homework;

public class Homework {
    
    String s, s1, s2;
    int[][] checked;

    public Homework(String s, String s1, String s2)
    {
        this.s = s;
        this.s1 = s1;
        this.s2 = s2;   
        this.checked = new int[s1.length()+1][s2.length()+1];
    }
    
    public boolean compute(int i, int j)
    {
    	if (checked[i][j] == 1)
    	{
    		return false;
    	}
    	else 
    	{
    		checked[i][j] = 1;
    	}
    	if (i == 0)
    	{	
    		return (s.substring(0, j).equals(s2.substring(0, j))) ? true : false;
    	}
    	if (j == 0)
    	{
    		return (s.substring(0, i).equals(s1.substring(0, i))) ? true : false;
    	}
    	
    	char s_char = s.charAt(i+j-1);
    	char s1_char = s1.charAt(i-1);
    	char s2_char = s2.charAt(j-1);
    	
        if (s_char != s1_char)
        {
            return (s_char != s2_char) ? false : compute(i, j-1);
        }
        else if (s_char != s2_char)
        {
            return (s_char != s1_char) ? false : compute(i-1, j);
        }
        else
        {
        	return compute(i, j-1) || compute(i-1, j);
        }
    }
    
    public String solve()
    {
    	return compute(s1.length(), s2.length()) ? "yes" : "no";
    }
}