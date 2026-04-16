class Solution {
    public int calPoints(String[] ops) {
        int[] st = new int[ops.length];
        int top = -1;

        for (String op : ops) {
            if (op.equals("+")) {
                st[++top] = st[top - 1] + st[top - 2];
            } 
            else if (op.equals("D")) {
                st[++top] = 2 * st[top - 1];
            } 
            else if (op.equals("C")) {
                top--; // remove last
            } 
            else {
                st[++top] = Integer.parseInt(op);
            }
        }

        int sum = 0;
        for (int i = 0; i <= top; i++) {
            sum += st[i];
        }

        return sum;
    }
}