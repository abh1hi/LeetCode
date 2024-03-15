#Given a string s, find the length of the longest substrig without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Dictionary to store the index of characters
        max_length = 0  # Maximum length of substring without repeating characters
        start_index = 0  # Starting index of the current substring

        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start_index:
                # If the character is seen again in the current substring
                start_index = char_index[char] + 1

            char_index[char] = i  # Update the latest index of the character
            max_length = max(max_length, i - start_index + 1)

        return max_length
