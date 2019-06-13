package kth.BurrowsWheeler;

import kth.BurrowsWheeler.SuffixArray;
import java.util.Scanner;

public class BW 
{
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args)
    {
		while (sc.hasNextLine())
		{
	       	String message = sc.nextLine();
	       	message += message;
	       	SuffixArray sa = new SuffixArray(message);

	       	for (int i = 0; i < sa.size(); i++)
	       	{
	       		int sf = sa.getSuffix(i);
	       		if (sf > 0 && sf < message.length()/2)
	       		{
	       			System.out.print(message.charAt(sa.getSuffix(i) - 1));
	       		}
	       		else if (sf == 0)
	       		{
	       			System.out.print(message.charAt(message.length() - 1));
	       		}
	       	}
	       	System.out.println("");      
		}
    }
}