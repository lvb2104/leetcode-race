public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var d = new Dictionary<int, int>();
        foreach (var x in nums)
        {
            d[x] = d.ContainsKey(x) ? d[x] + 1 : 1;
        }
        var temp = new List<KeyValuePair<int, int>>(d);
        temp.Sort((a, b) => b.Value.CompareTo(a.Value));
        var res = new int[k];
        foreach (var x in temp)
        {
            res[k - 1] = x.Key;
            k--;
            if (k == 0) break;
        }
        return res;
    }
}