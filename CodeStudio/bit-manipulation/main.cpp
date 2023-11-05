vector<int> bitManipulation(int n, int i){

    int res1 = n >> (i-1) & 1;
    int res2 = 1 << (i-1) | n;
    int res3 = ~(1 << (i-1)) & n;

    return {res1, res2, res3};
    
}