class MyQueue {

private:
    stack<int> st;
    stack<int> temp;
public:
    MyQueue() {
    }

    // [1, 2, 3, 4, 5]
    //  qh          sh

    // [5, 4, 3, 2, 1]
    //              qh
    //              sh

    void push(int x) {
    
        while(!st.empty()) {
            temp.push(st.top());
            st.pop();
        }

        st.push(x);

        while(!temp.empty()) {
            st.push(temp.top());
            temp.pop();
        }

    }
    
    int pop() {
        int val = st.top();
        st.pop();
        return val;
    }
    
    int peek() {
        return st.top();
    }
    
    bool empty() {
        return st.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
