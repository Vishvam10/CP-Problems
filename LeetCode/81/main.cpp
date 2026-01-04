class Solution {
public:
    bool search(vector<int>& arr, int target) {

        int n = arr.size();
        int low = 0, high = n - 1;

        if(n == 1) { 
            return arr[0] == target; 
        } else if(n == 2) { 
            return arr[0] == target || arr[1] == target; 
        }

        while(low <= high) {
            int mid = low + (high - low) / 2;

            if(arr[mid] == target) {
                return true;
            }

            if(arr[low] == arr[mid]) {
                low++;
                continue;
            }

            // check in left half
            if(arr[low] < arr[mid]) {
                if(target >= arr[low] && target < arr[mid]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } 
            // check in right half
            else {
                if(target > arr[mid] && target <= arr[high]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }

        }

        return false;
        
    }
};