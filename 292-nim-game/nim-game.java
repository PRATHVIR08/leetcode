class Solution {
    public boolean canWinNim(int n) {
        while(n > 0) {
            if(n < 4) return true;
            n -= 4;
        }
        return false;
    }
}