public class Solution {
    public int SingleNumber(int[] nums) {
        Dictionary<int, int> dict = new Dictionary<int, int>(); 

        foreach(int num in nums){
            if(!dict.ContainsKey(num)){
                dict.Add(num, 1); 
            }
            else{
                dict[num]++; 
            } 
        }
        var sorted_dict = dict.OrderBy(dict=> dict.Value);
        var integer = sorted_dict.ElementAt(0); 
        return integer.Key; 


    }
}
