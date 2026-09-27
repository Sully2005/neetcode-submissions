
public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length){
            return false;
        }
        Dictionary<char, int> dict = new Dictionary<char, int>();

    foreach(char c in s){
        if(dict.ContainsKey(c)){
            dict[c]++;
        }
        else{
            dict.Add(c,1);
        }
    }

    foreach(char c in t){
        if(dict.ContainsKey(c)){
            dict[c]--;
            if(dict[c] < 0){
                return false;
            }
        }
        else{
            return false;
        }
    }
    return true;
        }
    }
