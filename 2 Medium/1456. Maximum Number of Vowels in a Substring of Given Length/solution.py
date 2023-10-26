class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_letters = {'a', 'e', 'i', 'o', 'u'}
        vowel_counter = 0
        for i in range(k):
            if s[i] in vowel_letters:
                vowel_counter += 1
        
        Max_vowel_counter = vowel_counter
        left = 0
        for right in range(k, len(s)):
            first_char_in_window = s[left]
            if first_char_in_window in vowel_letters:
                vowel_counter -= 1
            last_char_in_window = s[right]
            if last_char_in_window in vowel_letters:
                vowel_counter += 1
            if Max_vowel_counter < vowel_counter:
                Max_vowel_counter = vowel_counter
            left += 1
        
        return Max_vowel_counter
