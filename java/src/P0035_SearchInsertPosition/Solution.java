package P0035_SearchInsertPosition;

public class Solution {
    public int searchInsert(int[] nums, int target) {
        int target_index = -1;
        int left = 0;
        int right = nums.length - 1;
        boolean search_position_ongoing = true;

        while (left <= right && search_position_ongoing){
            int center = (right + left)/2;
            if(nums[center] > target){
                right = center - 1;
            }
            else if(nums[center] < target){
                left = center + 1;
            }
            else{
                target_index = center;
                search_position_ongoing = false;
            }

        }

        if(target_index == - 1){
            return left;
        }
        else{
            return target_index;
        }
    }
}





