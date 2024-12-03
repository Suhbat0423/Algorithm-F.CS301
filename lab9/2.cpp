class MyStack {
public:
    queue<int> a;

    MyStack() {
        
    }
    
    void push(int x) {
        a.push(x);
        int n = a.size(); 

        for(int i=0; i<n-1; i++){
            a.push(a.front());
            a.pop();
        }
    }
    
    int pop() {
        int result = a.front();
        a.pop();

        return result;
    }
    
    int top() {
        return a.front();
    }
    
    bool empty() {
        return a.empty();
    }
};