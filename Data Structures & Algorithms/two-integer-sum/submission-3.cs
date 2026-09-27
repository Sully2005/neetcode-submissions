public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        List<int> termsList = new List<int>();
        for (int i = 0; i < nums.Length; i++){
            int real_target = target - nums[i];
            for(int j = i + 1; j < nums.Length; j++){
                if(nums[j] == real_target){
                    termsList.Add(i);
                    termsList.Add(j);
                }
            }
        }
        return termsList.ToArray();
    }
}
