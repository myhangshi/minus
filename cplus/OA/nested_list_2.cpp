/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer,
 *     // rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds,
 *     // if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds,
 *     // if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
private: 
    stack<int> st; 
    
    void push_elems(NestedInteger & elem) {
        if (elem.isInteger()) { 
            st.push(elem.getInteger()); 
        } else { 
            vector<NestedInteger> lst = elem.getList(); 
            for (int i = lst.size()-1; i >= 0; --i) { 
                push_elems(lst[i]); 
            } 
        }          
    } 
    
    
    void my_push_elems(NestedInteger & elem) {
        if (elem.isInteger()) { 
            nst.push(elem.getInteger()); 
        } else { 
            vector<NestedInteger> vst = elem.getList(); 
            for (int i = vst.size()-1; i >= 0; --i) { 
                my_push_elems(vst[i]); 
            } 
        }          
    } 
    
    void push_next() { 
        if (idx < lst.size()) { 
            my_push_elems(lst[idx]);
            idx++; 
        }
    }
    
    stack<int> nst; 
    int idx = 0; 
    vector<NestedInteger> &lst; 
    
public:
    NestedIterator(vector<NestedInteger> &nestedList):lst(nestedList) {
        // Initialize your data structure here.
        //lst = nestedList; 
        push_next();     
    }

    // @return {int} the next element in the iteration
    int next() {
        // Write your code here
        /* NestedInteger & elem = st.top(); st.pop();  
        
        if (elem.isInteger()) return elem.getInteger(); 
        else push_elems(elem.getList()); */ 
        if (nst.empty()) { 
            return INT_MIN; //throw exception 
        } 
        
        int elem = nst.top(); nst.pop(); 
        if (nst.empty()) { 
            push_next(); 
        } 
        
        return elem; 
    }

    // @return {boolean} true if the iteration has more element or false
    bool hasNext() {
        // Write your code here
        return !nst.empty(); 
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) v.push_back(i.next());
 */
