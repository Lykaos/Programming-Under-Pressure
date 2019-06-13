#include <iostream>
#include <bits/stdc++.h>

#define for(x,n) for(int x = 0; x < n; ++x)

using namespace std;

int solve(int N, int M, int priceA, int priceB)
{
    int cost = 0;
    while (1)
    {
        if (N == M)
        {
            return cost;
        }
        if (N/2 >= M && (N - N/2) * priceA > priceB)
        {
            cost += priceB;
            N = N/2;
        }
        else
        {
            cost += priceA * (N - M);
            return cost;
        }
    }
    return cost;
}

int main()
{
    int n_tests, N, M, L, cost;
    char names[101][29];
    int priceA[101], priceB[101];
    vector<tuple<int, string>> v;

    scanf("%d ", &n_tests);
    for(i, n_tests)
    {
        scanf("%d %d %d ", &N, &M, &L);
        cout << "Case " << i+1 << endl;
        for(j, L)
        {
            scanf("%[^:]: %d, %d ", names[j], &priceA[j], &priceB[j]);
            cost = solve(N, M, priceA[j], priceB[j]);
            v.push_back(make_tuple(cost, names[j]));
        }
        sort(v.begin(), v.end()); 
        for(j, v.size())
        {
            cout << get<1>(v[j]) << " " << get<0>(v[j]) << endl;
        }
        v.clear();
    }
    return 0;
}