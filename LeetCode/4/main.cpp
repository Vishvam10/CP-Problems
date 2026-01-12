class Solution {
public:
  /*

      Idea is to do binary search on "how many elements to pick" from
      arr1 (or arr2 depending on which is smaller). Min of elements we
      can pick = 0 and max no. of elements we can pick = min(n1, n2)

      The bs idea technically does a partition in this manner :
      Split arr1 and arr2 into 2 halves.
      Left half of arr1 and arr2 should be sorted
      Right half of arr1 and arr2 should be sorted
      (When these 2 are achieved, the combined array is sorted)

      This way, the median lies at the boundary between the two halves.
      To decide the elimation condition, we use the elements at the
      boundary of both arrays

      For eg. arr1 = 1 7 8 9 10 11 and arr2 = 4 5 6 7 8 10 12 15

      Initially, mid will be at index 2 :

      l1   r1
      1 7 8 | 9 10 11
      4 5 6 | 7 8 10 12 15
          l2  r2


      l1 > r2 => high = mid - 1.
      MEANING : We can't have a cut that big in arr1, so reduce it

      Similarly, l2 > r1 : low = mid + 1
      MEANING : We can't have a cut that small in arr1, so reduce it

      REASON for those 2 conditions : The current config won't have a
      sorted array in the end. Anyhow, only if both are false, we
      return the median

  */

  double findMedianSortedArrays(vector<int> &arr1, vector<int> &arr2) {
    int n1 = arr1.size(), n2 = arr2.size();
    int n = n1 + n2;

    if (n1 > n2) {
      return findMedianSortedArrays(arr2, arr1);
    }

    int low = 0, high = n1;

    while (low <= high) {

      // Total no. of elements that we PICK from arr1 (or arr2)
      int mid1 = low + (high - low) / 2;

      // Total no. of elements that we PICK from arr2 (or arr1)
      int mid2 = ((n + 1) / 2) - mid1;

      // These may not exist at times when we make cuts at the edges,
      // so initalizing them

      int l1 = (mid1 == 0) ? INT_MIN : arr1[mid1 - 1];
      int l2 = (mid2 == 0) ? INT_MIN : arr2[mid2 - 1];

      int r1 = (mid1 == n1) ? INT_MAX : arr1[mid1];
      int r2 = (mid2 == n2) ? INT_MAX : arr2[mid2];

      if (l1 <= r2 && l2 <= r1) {
        if (n % 2 == 0) {
          return (max(l1, l2) + min(r1, r2)) / 2.0;
        } else {
          return max(l1, l2);
        }
      } else if (l1 > r2) {
        high = mid1 - 1;
      } else {
        low = mid1 + 1;
      }
    }

    return 0.0;
  }
};