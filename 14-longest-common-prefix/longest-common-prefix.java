class Solution {
    public String longestCommonPrefix(String[] strs) {
        int n=strs.length;
        int min=100;
        int index=-1;
        for(int i=0;i<n;i++){
            min = Math.min(min, strs[i].length());
        }
        String s3="";
        for(int i=0;i<min;i++){
            char ch=strs[0].charAt(i);
            for(int j=1;j<n;j++){
                if(strs[j].charAt(i)!=ch){
                    return s3;
                }
            }
            s3=s3+ch;
        } 
        return s3;
    }
}