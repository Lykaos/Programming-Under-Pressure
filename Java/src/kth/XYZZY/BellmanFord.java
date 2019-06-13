/*
 * Course: Problem Solving and Programming under Pressure (DD2458)
 * Type: Laboratory exercises
 * Authors:
 * - Eduardo Rodes Pastor (9406031931)
 * - Florian Cassayre (980703T092)
 */
package kth.XYZZY;

import java.util.*;

public final class BellmanFord {
    private BellmanFord() {}

    /**
     * Computes all the shortest paths from a single source.
     * Negative weights are allowed, and negative cycle will be detected.
     * @param n the number of vertices
     * @param edges the edges
     * @param s the source vertex
     * @return a solution containing the costs and the paths;
     * a distance of <code>Integer.MAX_VALUE</code> indicates an impossible path
     * while <code>Integer.MIN_VALUE</code> means that the cost of the path can be
     * made arbitrarily low. The paths are stored in a tree
     */
    public static Solution shortestPath(int n, List<Edge> edges, int s) {
        final int[] distances = new int[n], parents = new int[n];
        final int[] energies = new int[n];

        // Initialization
        for(int i = 0; i < n; i++) 
        {
            distances[i] = Integer.MAX_VALUE;
            parents[i] = -1;
            energies[i] = -1;
        }

        distances[s] = 0; // Source
        energies[s] = 100;

        List<Integer> negative = new ArrayList<>();
        final BitSet visitedCycles = new BitSet();

        // Relaxation
        for (int i = 0; i <= n; i++)
        {
            for(Edge edge : edges)
            {       
                if(energies[edge.u] - edge.weight > 0 && distances[edge.u] < Integer.MAX_VALUE && distances[edge.u] + edge.weight < distances[edge.v]) {
                	energies[edge.v] = Math.max(energies[edge.v], energies[edge.u] - edge.weight);
                	distances[edge.v] = distances[edge.u] + edge.weight;
                    parents[edge.v] = edge.u;
                    if(i == n) { // Perform one more iteration to locate the vertices affected by negative cycles
                        negative.add(edge.v);
                        visitedCycles.set(edge.v);
                    }
                }
            }
        }
        final Map<Integer, List<Integer>> adjacency = new HashMap<>();
        for(int i = 0; i < n; i++)
            adjacency.put(i, new ArrayList<>());
        for(Edge edge : edges)
            adjacency.get(edge.u).add(edge.v);

        // Negative cycles
        while(!negative.isEmpty()) { // BFS
            final List<Integer> temp = new ArrayList<>();
            for(Integer u : negative) {
                distances[u] = Integer.MIN_VALUE;
                for(Integer v : adjacency.get(u))
                    if(!visitedCycles.get(v)) {
                        temp.add(v);
                        visitedCycles.set(v);
                    }
            }
            negative = temp;
        }

        return new Solution(n, distances, parents);
    }

    public static final class Solution {
        public final int n;
        public final int[] distances, parents;

        private Solution(int n, int[] distances, int[] parents) {
            this.n = n;
            this.distances = distances;
            this.parents = parents;
        }
    }

    public static final class Edge {
        public final int u, v;
        public int weight;

        public Edge(int u, int v, int weight) {
            this.u = u;
            this.v = v;
            this.weight = weight;
        }
    }
}