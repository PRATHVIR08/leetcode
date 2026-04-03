class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        for (int i = 0 ; i < s.length(); i++) {
            Set<Character> subStr = new HashSet<>();
            for (int x = i ; x < s.length(); x++) {
                if (!subStr.add(s.charAt(x))) {
                    break;
                }
            }
            longest = Math.max(longest, subStr.size());
        }

        return longest;
        
    }
}