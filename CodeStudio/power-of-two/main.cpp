bool isPowerOfTwo(int n)
{	
    int mask = (n-1);
    int res = n & mask;
    if(res == 0) {
        return true;
    }
    return false;
}