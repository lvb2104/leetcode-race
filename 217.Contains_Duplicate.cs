public class Solution
{
    public bool ContainsDuplicate(int[] nums)
    {
        var s = new HashSet<int>(nums);
        return s.Count != nums.Length;
    }
}