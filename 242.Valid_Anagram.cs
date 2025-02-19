public class Solution
{
    public bool IsAnagram(string s, string t)
    {
        var cnt = new int[123];
        foreach (var x in s) cnt[x]++;
        foreach (var x in t) cnt[x]--;
        foreach (var x in cnt) if (x != 0) return false;
        return true;
    }
}