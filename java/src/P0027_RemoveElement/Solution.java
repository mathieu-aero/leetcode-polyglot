package P0027_RemoveElement;

public class Solution {

    public int removeElement(int[] nums, int val) {
        int scout_index = 0;
        int write_index = 0;
        int max_length = nums.length;

        while (scout_index < max_length)
        {
            if(nums[scout_index] == val){
                scout_index += 1;
            }
            else{
                nums[write_index] = nums[scout_index];
                write_index += 1;
                scout_index += 1;
            }
        }

        return write_index;
    }
}



