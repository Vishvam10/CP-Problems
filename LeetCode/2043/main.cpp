class Bank {
public:
  unordered_map<int, long long> mp;

  Bank(vector<long long> &arr) {

    for (size_t i = 0; i < arr.size(); i++) {
      mp[i + 1] = arr[i];
    }
  }

  bool present(int acc) { return mp.find(acc) != mp.end(); }

  bool transfer(int account1, int account2, long long money) {
    if (this->present(account1) && this->present(account2) &&
        mp[account1] >= money) {
      mp[account1] -= money;
      mp[account2] += money;
      return true;
    }
    return false;
  }

  bool deposit(int account, long long money) {
    if (this->present(account)) {
      mp[account] += money;
      return true;
    }
    return false;
  }

  bool withdraw(int account, long long money) {
    if (this->present(account) && mp[account] >= money) {
      mp[account] -= money;
      return true;
    }
    return false;
  }
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */