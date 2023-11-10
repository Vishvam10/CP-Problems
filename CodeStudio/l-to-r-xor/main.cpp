int XOR(int n) {
    int rem = n & 3;    // rem = n % 4
    if(rem == 0) {
        return n;
    } else if(rem == 1) {
        return 1;
    } else if(rem == 2) {
        return n + 1;
    } else {
        return 0;
    }
}

int findXOR(int l, int r){
    int mask1 = XOR(l-1);
    int mask2 = XOR(r);
    int ans = mask1 ^ mask2;
    return ans;
}