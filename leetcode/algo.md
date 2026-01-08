krushkals
#include <bits/stdc++.h>
using namespace std;
/* ===================== DSU CLASS ===================== */
class DisjointSet {
    vector<int> parent, rank;
public:
    DisjointSet(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++)
            parent[i] = i;
    }
    // Find with path compression
    int findUPar(int node) {
        if (node == parent[node])
            return node;
        return parent[node] = findUPar(parent[node]);
    }
    // Union by rank
    void unionByRank(int u, int v) {
        int pu = findUPar(u);
        int pv = findUPar(v);
        if (pu == pv) return;
        if (rank[pu] < rank[pv]) {
            parent[pu] = pv;
        } else if (rank[pv] < rank[pu]) {
            parent[pv] = pu;
        } else {
            parent[pv] = pu;
            rank[pu]++;
        }
    }
};
/* ===================== KRUSKAL ===================== */
int main() {
    int V, E;
    cin >> V >> E;
    vector<pair<int, pair<int, int>>> edges;
    // Input edges: u v weight
    for (int i = 0; i < E; i++) {
        int u, v, wt;
        cin >> u >> v >> wt;
        edges.push_back({wt, {u, v}});
    }
    // Sort edges by weight
    sort(edges.begin(), edges.end());
    DisjointSet ds(V);
    int mstWeight = 0;
    vector<pair<int,int>> mstEdges;
    for (auto &edge : edges) {
        int wt = edge.first;
        int u = edge.second.first;
        int v = edge.second.second;
        if (ds.findUPar(u) != ds.findUPar(v)) {
            mstWeight += wt;
            mstEdges.push_back({u, v});
            ds.unionByRank(u, v);
        }
    }
    // Output
    cout << "MST Weight: " << mstWeight << "\n";
    cout << "Edges in MST:\n";
    for (auto &e : mstEdges) {
        cout << e.first << " - " << e.second << "\n";
    }
    return 0;
}




//problem set to follow
https://cses.fi/problemset/