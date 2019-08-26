/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    let [start, end] = [1, nums.length]
    let mid = end;
    nums.unshift(-Infinity);
    nums.push(-Infinity);
    while (start < end) {
        if (nums[end] > nums[mid]) {
            start = mid + 1;
        } else {
            end = mid;
        }
        mid = parseInt((end + start) / 2); 
    }
    return mid - 1;
}