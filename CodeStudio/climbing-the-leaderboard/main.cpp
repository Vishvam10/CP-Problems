#include <bits/stdc++.h> 
vector<int> findPosition(vector<int> arr, int n, vector<int> playerScore, int m) {

    vector<int> ranks;
    vector<int> ans;    

    ranks.emplace_back(arr[0]);

    for(int i=1; i<n; i++) {
        if(arr[i-1] != arr[i]) {
            ranks.emplace_back(arr[i]);
        }
    }

    int i = ranks.size() - 1;

    for(auto score: playerScore) {
        while(i >= 0 && score >= ranks[i]) {
            i--;
        }
        ans.emplace_back(i+2);
    }

    return ans;

}
