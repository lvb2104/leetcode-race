public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var d = new Dictionary<int, int>();
        for (var i = 0; i < nums.Length; i++)
        {
            if (d.ContainsKey(target - nums[i]))
                return [d[target - nums[i]], i];
            d[nums[i]] = i;
        }
        return [-1, -1];
    }
}
