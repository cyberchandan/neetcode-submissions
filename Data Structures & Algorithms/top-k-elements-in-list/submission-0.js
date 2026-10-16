class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        // Step 1: Create a frequency map
        let hashMap = new Map();

        for (let number of nums) {
            // If number already exists, increase count; else set to 1
            hashMap.set(number, (hashMap.has(number) ? hashMap.get(number) : 0) + 1);
        }

        // Step 2: Convert map entries to an array and sort by frequency descending
        let sortedArr = Array.from(hashMap.entries()).sort((a, b) => b[1] - a[1]);

        // Step 3: Take top k elements and return only the numbers (keys)
        return sortedArr.slice(0, k).map(e => e[0]);
    }
}
