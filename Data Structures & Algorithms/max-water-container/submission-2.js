class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let left = 0
        let right = heights.length - 1
        let maxWater = 0
        let width
        let length
        while (left < right) {
            if (heights[left] > heights[right]) {
                length = heights[right]
            } else {
                length = heights[left]
            }
            width = right - left
            let area = length * width
            if (area > maxWater) {
                maxWater = area
            }

            if (heights[left] < heights[right]) {
                left++
            } else {
                right--
            }
        }
        return maxWater
    }
}