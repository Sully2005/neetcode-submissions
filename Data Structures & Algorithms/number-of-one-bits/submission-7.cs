public class Solution {
    public int HammingWeight(uint n) {
        int count = 0; 
        int i = 0; 
        uint mask = 1;
        while(i != 32){
            if( ((n >> i) & mask) == mask ){
                count++; 
            }
            i++;
        }
        return count; 
    }
}
