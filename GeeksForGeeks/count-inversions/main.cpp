typedef long long ll;

class Solution
{
public:
    
    ll c = 0;

    void merge(ll arr[], ll low, ll mid, ll high)
    {
        vector<ll> temp;
        ll left = low;
        ll right = mid + 1;
        while (left <= mid and right <= high)
        {
            if (arr[left] <= arr[right])
            {
                temp.push_back(arr[left]);
                left++;
            }
            else
            {
                temp.push_back(arr[right]);
                c = c + (mid - left + 1);
                right++;
            }
        }

        while (left <= mid)
        {
            temp.push_back(arr[left]);
            left++;
        }
        
        while (right <= high)
        {
            temp.push_back(arr[right]);
            right++;
        }
        
        // overwrite
        for (ll i = low; i <= high; i++)
        {
            arr[i] = temp[i - low];
        }
    }

    void mergesort(ll arr[], ll low, ll high)
    {
        if (low == high)
            return;
        ll mid = (low + high) / 2;
        mergesort(arr, low, mid);
        mergesort(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }

    ll inversionCount(ll arr[], ll N)
    {
        // Your Code Here
        mergesort(arr, 0, N - 1);
        return c;
    }

};