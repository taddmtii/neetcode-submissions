class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> nums_map;
        for (const auto& elem : nums) {
            if (nums_map.find(elem) == nums_map.end()) {
                nums_map[elem] = 1;
            }
            else {
                return true;
            }
        }
        return false;
    }
};