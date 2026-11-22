package P0001_TwoSum;
import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int[] twoSum(int[] nums, int target) {

        int i = 0;
        boolean solution_still_not_found = true;
        int index_first_number = 0;
        int index_second_number = 0;
        Map<Integer, Integer> values_considered = new HashMap<>();

        while (i < nums.length && solution_still_not_found){
            if (values_considered.containsKey(target - nums[i])){
                index_first_number = i;
                index_second_number = values_considered.get(target - nums[i]);
                solution_still_not_found = false;
            }
            else {
                values_considered.put(nums[i], i);
                i += 1;
            }
        }
        int[] result = {index_first_number, index_second_number};
        return result;
    }

}