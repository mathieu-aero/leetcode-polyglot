package P0026_RemoveDuplicatesFromSortedArray;

class Solution {
    public int removeDuplicates(int[] nums) {
        int scout_index = 1;
        int write_index = 0;
        int max_length = nums.length;

        while (scout_index < max_length){
            if(nums[write_index] == nums[scout_index]){
                scout_index += 1;
            }
            else{
                write_index += 1;
                nums[write_index] = nums[scout_index];
                scout_index += 1;
            }
        }
        return write_index + 1;
    }
}
