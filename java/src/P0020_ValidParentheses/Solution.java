package P0020_ValidParentheses;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;


class Solution {
    public boolean isValid(String s) {
        int max_length = s.length();
        int i = 0;

        Map<Character, Character> pairs = Map.of(
                '(', ')',
                '[', ']',
                '{', '}'
        );

        List<Character> pile = new ArrayList<>();

        boolean still_valid = true;

        if (max_length % 2 == 0) {
            while (i < max_length && still_valid) {
                char the_character = s.charAt(i);
                if (pairs.containsKey(the_character)) {
                    pile.add(pairs.get(the_character));
                } else {
                    if (pile.size() > 0 && pile.get(pile.size() - 1) == the_character) {
                        pile.remove(pile.size() - 1);
                    } else {
                        still_valid = false;
                    }
                }
                i += 1;
            }
            return still_valid && pile.size() == 0;
        }
        else return false;
    }
}