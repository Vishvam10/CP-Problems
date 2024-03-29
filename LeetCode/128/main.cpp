class Solution {
public:

    int longestConsecutive(vector<int>& arr) {
        
        int n = arr.size();
        int ans = 0;

        // init with arr[i] = true for all i in n
        unordered_map<int, bool> mp;

        for(int i = 0; i < n; i++) {
            mp[arr[i]] = true;
        }

        // basically find all the difference 1 elements
        // so target = 1, x = ele and we need to find
        // if ele - 1 is present in the array. if so, 
        // mark it as "NOT A STARTING POINT". 

        // this eliminates cycles and updating back/forward
        // references in the chain


        for(int i = 0; i < n; i++) {
            if(mp.find(arr[i] - 1) != mp.end()) {
                // can not be a starting point
                mp[arr[i]] = false;
            }
        }
        
        
        for(int i = 0; i < n; i++) {

            // checking only potential starting points
            if(mp[arr[i]] == true) {
                int count = 0;
                while(mp.find(arr[i] + count) != mp.end()) {
                    count++;
                }
                ans = max(ans, count);
            }   
        }

        return ans;


    }
}; 