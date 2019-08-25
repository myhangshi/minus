

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        int res = INT_MAX, cnt = 0;
        unordered_map<int, vector<vector<int>>> m;
        queue<vector<int>> q{{{src, 0}}};
        for (auto flight : flights) {
            m[flight[0]].push_back({flight[1], flight[2]});
        }
        while (!q.empty()) {
            for (int i = q.size(); i > 0; --i) {
                auto t = q.front(); q.pop();
                if (t[0] == dst) res = min(res, t[1]);
                for (auto a : m[t[0]]) {
                    if (t[1] + a[1] > res) continue;
                    q.push({a[0], t[1] + a[1]});
                }
            }
            if (cnt++ > K) break;
        }
        return (res == INT_MAX) ? -1 : res;
    }
};


