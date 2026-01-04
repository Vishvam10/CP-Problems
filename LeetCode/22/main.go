func gen(s string, open int, close int, n int, ans *[]string) {

    if len(s) == 2 * n {
        *ans = append(*ans, s)
        return
    }

    if open < n {
        gen(s + "(", open + 1, close, n, ans)
    }

    if close < open {
        gen(s + ")", open, close + 1, n, ans)
    }

}

func generateParenthesis(n int) []string {
    ans := []string{}
    gen("", 0, 0, n, &ans)
    return ans
}
