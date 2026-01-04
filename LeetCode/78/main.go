func gen(ind int, res []int, nums []int, ans *[][]int) {
    if ind == len(nums) {
        *ans = append(*ans, append([]int{}, res...))
        return
    }

    // Include
    gen(ind + 1, append(res, nums[ind]), nums, ans)
    
    // Exlude
    gen(ind + 1, res, nums, ans)
}


func subsets(nums []int) [][]int {
    ans := [][]int{}
    gen(0, []int{}, nums, &ans)
    return ans
}

