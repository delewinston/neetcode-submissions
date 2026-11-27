class Solution {
    public int longestConsecutive(int[] nums) {
        java.util.Set<Integer> set = new java.util.HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        int best = 0;

        for (int num : set) {
            if (set.contains(num - 1)) {
                continue;   // not the start of a run
            }
            int length = 1;
            while (set.contains(num + length)) {
                length++;
            }
            best = Math.max(best, length);
        }

        return best;
    }
}