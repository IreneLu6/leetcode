class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> my_map;
        for (int i = 0; i < nums.size(); i++) {
            auto it = my_map.find(target - nums[i]);
            if (it != my_map.end()) {
                return {it->second, i};
            }
            my_map[nums[i]] = i;
        }
    };
}