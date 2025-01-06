//
// Created by Irene Lu on 2025/1/6.
//
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map <string, vector<string>> my_map;
        vector<vector<string>> my_v;
        for (int i = 0; i < strs.size(); i++)
        {
            string tmp( strs[i]);
            sort(strs[i].begin(),strs[i].end());
            my_map[strs[i]].push_back(tmp);
        }
        for (auto it = my_map.begin(); it != my_map.end(); it++)
        {
            my_v. push_back (it->second);
        }
        return my_v;}
};