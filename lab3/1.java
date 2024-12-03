class Solution {
    public int majorityElement(int[] nums) {
        return majorityElementRec(nums, 0, nums.length - 1);
    }
    private int majorityElementRec(int[] nums, int lo, int hi) {
        if (lo == hi) {
            return nums[lo];
        }
        int mid = lo + (hi - lo) / 2;
        int leftMajor = majorityElementRec(nums, lo, mid);
        int rightMajor = majorityElementRec(nums, mid + 1, hi);
        if (leftMajor == rightMajor) {
            return leftMajor;
        }
        int leftCount = countInRange(nums, leftMajor, lo, hi);
        int rightCount = countInRange(nums, rightMajor, lo, hi);
        return leftCount > rightCount ? leftMajor : rightMajor;
    }
    private int countInRange(int[] nums, int num, int lo, int hi) {
        int count = 0;
        for (int i = lo; i <= hi; i++) {
            if (nums[i] == num) {
                count++;
            }
        }
        return count;
    }
}
