class Solution {
public:

    void merge(vector<pair<int, int>>& arr, int low, int mid, int high, vector<int>& ans) {

        int i = low, j = mid + 1;
        vector<pair<int, int>> temp;

        while(i <= mid && j <= high) {
            if(arr[i].first <= arr[j].first) {
                temp.emplace_back(arr[j]);
                j++;
            } else {
                temp.emplace_back(arr[i]);
                ans[arr[i].second] += (high - j + 1);
                i++;
            }
        }

        while(i <= mid) {
            temp.emplace_back(arr[i++]);
        }

        while(j <= high) {
            temp.emplace_back(arr[j++]);
        }

        // overwrite
        for(int i = low; i <= high; i++) {
            arr[i] = temp[i - low];
        }       

        return;

    }

    void mergeSort(vector<pair<int, int>>& arr, int low, int high, vector<int>& ans) {
        if(low >= high) {
            return;
        }

        int mid = low + (high - low) / 2;
        mergeSort(arr, low, mid, ans);
        mergeSort(arr, mid + 1, high, ans);
        merge(arr, low, mid, high, ans);

        return;

    }


    vector<int> countSmaller(vector<int>& a) {
        
        // [5, 5, 4] and [6, 5, 4, 3, 2, 2, 1]
        int n = a.size();
        vector<pair<int, int>> arr;
        vector<int> ans(n, 0);

        for(int i = 0; i < n; i++) {
            // we need to keep track of the original index
            // emplace_back needs either make_pair(a, b) or no braces
            arr.emplace_back(a[i], i);
        }

        mergeSort(arr, 0, n - 1, ans);
        return ans;

    }
};