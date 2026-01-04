func isPowerOfTwo(n int) bool {

    // 8 := 1 0 0 0
    // 7 := 0 1 1 1
    // 8 & 7 = 0 .. so power of 2 ?
    
    return n > 0 && (n & (n - 1)) == 0
}
