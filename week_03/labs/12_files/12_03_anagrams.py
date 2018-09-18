

"""
12_03 - had a wierd ASCII error in this text - so removed it.
"""
import anagram_sets

if __name__ == '__main__':
    anagram_map = anagram_sets.all_anagrams('12_files/words2.txt')
    anagram_sets.print_anagram_sets_in_order(anagram_map)
