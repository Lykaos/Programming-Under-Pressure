package kth.herkabe;

import java.util.List;

public class Solver 
{  
    List<String> w;
    int[] fact = { 0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 227020758, 178290591, 674358851, 
            789741546, 425606191, 660911389, 557316307, 146326063, 72847302, 602640637, 860734560, 657629300, 440732388, 459042011, 394134213 };
    int mod = 1000000007;
    
    public Solver(List<String> w)
    {
        this.w = w;
    }

    public long solve(int pos1, int pos2, int ch)
    {
        if (pos2 - pos1 < 3)
        {
            return pos2 - pos1;
        }
        long res = 1;
        int n_groups = 0;
        for (int i = pos1 + 1; i < pos2; i++)
        {
            String word1 = w.get(i-1);
            String word2 = w.get(i);
            if (word1.length() == ch || (word1.charAt(ch) != word2.charAt(ch)))
            {
                n_groups++;
                res = res * solve(pos1, i, ch + 1) % mod;
                pos1 = i;
            }
        }
        res = res * solve(pos1, pos2, ch + 1) % mod;
        res = res * fact[n_groups+1] % mod;
        return res;
    } 
}