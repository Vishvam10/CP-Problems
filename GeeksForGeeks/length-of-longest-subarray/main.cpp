long long int longestSubarry(long long int arr[], long long int n) {
    
    long long int count = 0, mx = 0;
    
    for(int i = 0; i < n; i++) {
        if(arr[i] < 0) {
            mx = max(mx, count);
            count = 0;
        } else {
            count++;
        }
    }
    
    return max(mx, count);
}