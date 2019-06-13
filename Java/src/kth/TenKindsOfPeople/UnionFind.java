/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */
package kth.TenKindsOfPeople;

public final class UnionFind {

    private final int[] parents; // The parent of each element (or itself if singleton)
    private final int[] ranks; // The rank of each element (initially 0)

    /**
     * Creates a new a forest of <code>n</code> singleton sets.
     * @param n the number of elements in the forest
     */
    public UnionFind(int n) {
        parents = new int[n];
        ranks = new int[n];

        for(int i = 0; i < n; i++) {
            parents[i] = i;
            ranks[i] = 0;
        }
    }

    /**
     * Merge the two sets together.
     * @param a the set containing the element a
     * @param b the set containing the element b
     */
    public void union(int a, int b) {
        checkArguments(a, b);

        int ar = find(a), br = find(b);
        if(ar != br) {
            if(ranks[ar] < ranks[br]) {
                parents[ar] = br;
            } else {
                parents[br] = ar;
                if(ranks[ar] == ranks[br]) {
                    ranks[ar] += 1;
                }
            }
        }
    }

    /**
     * Checks if the two elements are in the same set.
     * @param a the first element
     * @param b the second element
     * @return a boolean corresponding to the result
     */
    public boolean same(int a, int b) {
        checkArguments(a, b);

        return find(a) == find(b);
    }

    /**
     * Finds the parent of this element and compresses the path if necessary.
     * @param x the element to find the parent of
     * @return the parent of this element
     */
    private int find(int x) {
        if(parents[x] != x) {
            parents[x] = find(parents[x]);
        }
        return parents[x];
    }

    /**
     * Checks if the arguments are effectively elements of the forest.
     * @param a the first element
     * @param b the second element
     */
    private void checkArguments(int a, int b) {
        if(a < 0 || a >= parents.length || b < 0 || b >= parents.length)
            throw new IllegalArgumentException();
    }
}