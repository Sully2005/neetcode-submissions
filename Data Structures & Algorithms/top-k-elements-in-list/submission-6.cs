public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary <int, int> map  = new Dictionary<int, int>(); 
        List<int> array = new List <int> {}; 
        foreach(int num in nums){
            if(!map.ContainsKey(num)){
                map.Add(num, 1);
            }
            else{
                map[num]++;
            }
        }
        // now we have a map of the occurances of every number 
        var sorted_map = map.OrderByDescending(map => map.Value);
        // once we have it sorted we can just go through it like a regular for loop
        for (int i = 0; i < k; i++){
            array.Add(sorted_map.ElementAt(i).Key);
        }
        return array.ToArray();
    }
}
