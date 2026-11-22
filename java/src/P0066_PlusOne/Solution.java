package P0066_PlusOne;

import java.util.ArrayList;
import java.util.List;

public class Solution {
        public int[] plusOne(int[] digits) {
            String initial_number = "";
            int final_number = 0;
            List<Integer> result = new ArrayList<>();

            for (int element:digits) {
                initial_number = initial_number + Integer.toString(element);
            }

            final_number = Integer.parseInt(initial_number) + 1;
            String final_string = Integer.toString(final_number);

            for (char letter:final_string.toCharArray()) {
                result.add(Character.getNumericValue(letter));
            }

            int[] output = new int[result.size()];
            for (int i = 0; i < result.size(); i++) {
                output[i] = result.get(i);
            }

            return output;
        }
    }

