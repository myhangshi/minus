/* 
    Compilation notes (MacOS, Xcode g++ 4.2.1, Apple LLVM version 10.0.1): 
        g++ -std=c++17 iv1.cpp
*/ 
#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

struct Node { 
    int val; 
    struct Node *left; 
    struct Node *right; 
}; 

struct QueueNode { 
    Node *node; 
    Node *parent; 
    //bool isLeft; 
}; 

Node* mirrorTree(Node *root) { 
    if (!root) { 
        return nullptr; 
    }

    Node * newRoot= new Node{root->val, nullptr, nullptr}; 

    newRoot->left = mirrorTree(root->right); 
    newRoot->right = mirrorTree(root->left); 

    return newRoot; 
}

/*
        0. create queue<Node*, Node*> q to record current node and its parent node
        1. create new root, enqueue (root, newroot)     
        2. dequeue for each queueNode 
        3.      get node of old tree node and its mapped node in the new node
        4.      if left node exists, 
                    allocate a new node for new tree
                    assign it as right child as the mapped node
                    enqueue (old left, mapped)
        5.      if right node exists
                    allocate a new node for new tree
                    assign it as right child as the mapped node
                    enqueue (old left, mapped) 
        6.        free node of old tree   
        7. return newRoot created in step 2 
    */ 
Node* mirrorTreeIterative(Node *root) {
    queue<QueueNode *> q; 

    if (root == nullptr) { 
        return nullptr; 
    }

    Node *newRoot = new Node{root->val, nullptr, nullptr}; 
    QueueNode *q1 = new QueueNode{root, newRoot}; 
    q.push(q1); 

    while (!q.empty()) { 
        QueueNode * q2 = q.front(); q.pop(); 
        //traversed nodes in old tree and new tree should not be null 
        assert(q2->node); 
        assert(q2->parent); 
    
         ; 
        // create mirror nodes for the left
        if (q2->node->left) { 
            Node *nRight = new Node{q2->node->left->val, nullptr, nullptr}; 
            q2->parent->right = nRight; 
            q.push(new QueueNode{q2->node->left, nRight}); 
        }    
        if (q2->node->right) { 
            Node *nLeft = new Node{q2->node->right->val, nullptr, nullptr};  
            q2->parent->left = nLeft;
            q.push(new QueueNode{q2->node->right, nLeft}); 
        }    

        delete q2; 
    }

    return newRoot; 
}  

bool isMirroredTree(Node *root1, Node *root2) { 
    if (!root1 && !root2) { 
        return true; 
    }

    if (!root1 || !root2) { 
        return false; 
    }

    if (root1->val != root2->val) { 
        return false; 
    }

    return isMirroredTree(root1->left, root2->right) && 
                isMirroredTree(root1->right, root2->left); 
}

int main() 
{ 
    cout << "mirrored tree generation: " << endl; 
    cout << "  recursive and iterative. " << endl; 
    
    /* A tree as below:  
     *              5 
     *            /    \
     *           4      3
     *                 /  \
     *                2    1
     */ 
    Node *p1 = new Node {1, nullptr, nullptr}; 
    Node *p2 = new Node {2, nullptr, nullptr}; 
    Node *p3 = new Node {3, p2, p1}; 
    Node *p4 = new Node {4, nullptr, nullptr}; 
    Node *p5 = new Node {5, p4, p3}; 
    
    bool isMirrored; 

    Node *newRoot = mirrorTree(p5); 
    isMirrored = isMirroredTree(newRoot, p5); 
    cout << "is Mirrored Tree " << isMirrored << endl; 

    Node *p6 = new Node{6, nullptr, nullptr}; 
    isMirrored = isMirroredTree(newRoot, p6); 
    cout << "is Mirrored Tree " << isMirrored << endl; 

    Node* p7 = mirrorTreeIterative(p5); 
    isMirrored = isMirroredTree(p7, p5); 
    cout << "is Mirrored Tree " << isMirrored << endl; 


    // TODO: need to delete the nodes allocated from 
    //     mirrorTree and mirrorTreeIterative 
    delete p1; 
    delete p2; 
    delete p3; 
    delete p4; 
    delete p5; 
    delete p6;   

    return 0; 
} 
