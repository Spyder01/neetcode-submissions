impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut left = 0;
        let mut right = nums.len().saturating_sub(1);

        while left < right {
            let sum = nums[left] + nums[right];

            if sum == target {
                return vec![left as i32 + 1, right as i32 + 1];
            } 

            if sum < target {
                left += 1;
            } else {
                right -= 1;
            }
        }

        Vec::new()
    }
}
