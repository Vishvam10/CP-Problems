vector<int> twoOddNum(vector<int> arr){
    int res = 0, res1 = 0, res2 = 0;

    for(int &x : arr) {
        res ^= x;
    }

    rmsb = x & ~(x - 1);

    for(int &x : arr) {
        if(x & rmsb) {
            res1 ^= x;
        } else {
            res2 ^= x;
        }
    }

    return {max(res1, res2), min(res1, res2)};

}