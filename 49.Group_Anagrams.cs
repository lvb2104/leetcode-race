public class Solution
{
    public IList<IList<string>> GroupAnagrams(string[] strs)
    {
        var d = new Dictionary<string, List<string>>();
        foreach (var str in strs)
        {
            var key = String.Concat(str.OrderBy(c => c));
            if (!d.ContainsKey(key))
            {
                d[key] = new List<string>();
            }
            d[key].Add(str);
        }
        return [.. d.Values];
    }
}