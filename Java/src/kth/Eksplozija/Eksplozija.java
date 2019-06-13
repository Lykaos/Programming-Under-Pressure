/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */
package kth.Eksplozija;

import kth.Kattio;

import java.util.ArrayList;
import java.util.List;

public class Eksplozija 
{
    public static void run(Kattio kattio) 
    {
        String word = kattio.getWord();
        String explosion = kattio.getWord();
        solve(word, explosion, kattio);
        kattio.close();
    }
    
    public static void solve(String word, String explosion, Kattio kattio)
    {
        if (explosion.length() == 1)
        {
            String result = word.replace(explosion, "");
            String output = (result.length() == 0) ? "FRULA" : result;
            kattio.println(output);
        }
        else
        {
            int pos = 0;
            List<Integer> stack = new ArrayList<Integer>();
            List<Integer> stack2 = new ArrayList<Integer>();

            int[] begin = new int[word.length()];
            int[] end = new int[word.length()];
           
            for (int i = 0; i < word.length(); i++)
            {
                char c = word.charAt(i);
                if (c == explosion.charAt(0))
                {
                    stack.add(i);
                    stack2.add(i);
                    pos = 1;
                }
                else if (stack.size() > 0)
                {
                    if (c == explosion.charAt(pos))
                    {
                        if (pos == explosion.length() - 1)
                        {
                        	begin[stack2.get(stack2.size() - 1)] += 1;
                        	end[i] += 1;
                            
                            stack.remove(stack.size() - 1);
                            stack2.remove(stack2.size() - 1);
                            
                            if (stack.size() > 0)
                            {
	                        	int last_i = stack.get(stack.size() - 1);
	                            pos = explosion.indexOf(word.charAt(last_i)) + 1;
                            }
                            else
                            {
                            	pos = 0;
                            }
                        }
                        else
                        {
                        	stack.set(stack.size() - 1, i);
                        	pos++;
                        }
                    }
                    else
                    {
                        stack = new ArrayList<Integer>();
                        stack2 = new ArrayList<Integer>();
                        pos = 0;
                    }
                }
            }
            
            int i = 0;
            int counter = 0;
            boolean not_empty = false;
            while (i < word.length())
            {
                if (begin[i] > 0) { counter++; }
                else if (end[i] > 0) { counter--; }
                else
                {
                    if (counter == 0)
                    {
                        kattio.print(word.charAt(i));
                        not_empty = true;
                    }
                }
                i++;
            }   
            if (!not_empty)
            {
                kattio.println("FRULA");
            }
        }

    }

    public static void main(String[] args) 
    {
        run(new Kattio());
    }
}