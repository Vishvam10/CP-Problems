class Solution {
public:
  int characterReplacement(string s, int k) {
    int n = s.length();
    int left = 0, maxFreq = 0, ans = 0;
    vector<int> freq(26, 0);

    // Why if not while AND why not update maxFreq inside if ?
    // REASON : For eg, k = 2 and at some point len of substr = 5 and
    // maxFreq = 3. To get a better answer (say, 6, 7, etc), we need
    // len to increase AND maxFreq to increase to maintin the
    // inequality. There's no point in decreasing the maxFreq (decrease
    // as that's what would've happened if we did a while loop on left
    // using the same conditioon) as (here, for instance) len = 6,
    // maxFreq = 2 WILL NEVER occur in the first place as the inequality
    // is broken

    for (int right = 0; right < n; ++right) {
      freq[s[right] - 'A']++;
      maxFreq = max(maxFreq, freq[s[right] - 'A']);

      if ((right - left + 1) - maxFreq > k) {
        freq[s[left] - 'A']--;
        left++;
      }

      ans = max(ans, right - left + 1);
    }
    return ans;
  }
};
