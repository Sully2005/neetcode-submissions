public class Solution {
    public int[] CountBits(int n) {
        int i = 0;
        int count = 0; 
        int temp; 
        int[] result = new int [n + 1]; 

        while(i <= n){
            temp = i; 
            while(temp != 0){
                temp &= (temp - 1); 
                count++; 
            }
            result[i] = count; 
            count = 0;
            i++; 
        }
        return result; 
    }
}
