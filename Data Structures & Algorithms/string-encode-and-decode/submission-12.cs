public class Solution {

  public string Encode(IList<string> strs)
{
    StringBuilder sb = new StringBuilder();

    foreach (string s in strs)
    {
        sb.Append(s.Length);
        sb.Append('#');
        sb.Append(s);
    }

    return sb.ToString();
}


    public List<string> Decode(string s)
{
    List<string> output = new List<string>();
    int i = 0;

    while (i < s.Length)
    {
        // 1. Read the length prefix
        int hashIndex = s.IndexOf('#', i);
        int length = int.Parse(s.Substring(i, hashIndex - i));

        // 2. Read the actual string
        string parsed = s.Substring(hashIndex + 1, length);
        output.Add(parsed);

        // 3. Move i forward
        i = hashIndex + 1 + length;
    }

    return output;
}
}