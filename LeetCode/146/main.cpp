class LRUCache {
public:
    
    class Node {
        public : 
            int key;
            int val;
            Node* next;
            Node*  prev;
        
        Node(int key, int val) {
            this->key = key;
            this->val = val;
        }
    };

    Node* head = new Node(-1, -1);
    Node* tail = new Node(-1, -1);

    unordered_map<int, Node*> mp;
    int cap;

    LRUCache(int capacity) {
        cap = capacity;
        head->next = tail;
        tail->prev = head;
    }
    
    void add_node(Node* nn) {
        Node* temp = head->next;
        nn->next = temp;
        nn->prev = head;

        head->next = nn;
        temp->prev = nn;
    }

    void delete_node(Node* nn) {
        nn->next->prev = nn->prev;
        nn->prev->next = nn->next;
    }
    
    int get(int key) {

        if(mp.find(key) != mp.end()) {
            
            Node* nn = mp[key];
            int res = nn->val;

            mp.erase(key);
            delete_node(nn);

            add_node(nn);
            mp[key] = head->next;

            return res;

        }

        return -1;
        
    }
    
    void put(int key, int value) {
        if(mp.find(key) != mp.end()) {
            Node* temp = mp[key];
            mp.erase(key);
            delete_node(temp);
        } else {
            if(mp.size() == cap) {
                Node* lru_node = tail->prev;
                mp.erase(lru_node->key);
                delete_node(lru_node);
            } 
        }
        Node* nn = new Node(key, value);
        add_node(nn);
        mp[key] = head->next;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */