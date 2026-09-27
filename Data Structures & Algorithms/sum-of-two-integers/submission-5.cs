
public class Solution{
public int GetSum(int a, int b)
{
    int carry = 0;
    int sum = 0;

    for (int i = 0; i < 32; i++)
    {
        int ai = (a >> i) & 1;
        int bi = (b >> i) & 1;

        int s = ai ^ bi ^ carry;
        int carry_out = (ai & bi) | (carry & (ai ^ bi));

        sum |= (s << i);
        carry = carry_out;
    }

    return sum;
}
}