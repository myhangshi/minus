/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;

    Node() {}

    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) { 
            return nullptr; 
        }
        
        unordered_map<Node*, Node*> mp; 
        queue<Node*> q; 
        
        mp[node] = new Node(node->val); 
        q.push(node); 
        
        while (!q.empty()) { 
            Node *p1 = q.front(); q.pop(); 
            
            for (auto nb: p1->neighbors) { 
                if (mp.find(nb) == mp.end()) { 
                    Node *newCur = new Node(nb->val); 
                    mp[nb] = newCur; 
                    q.push(nb); 
                }
                mp[p1]->neighbors.push_back(mp[nb]); 
            }
        
        }
        
        return mp[node]; 
    }
};

