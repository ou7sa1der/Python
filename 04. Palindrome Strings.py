sentances_string = input().split(' ')
palindrome_word = input()
times_of_occurancies = 0
palindrome_list = [word for word in sentances_string if word == palindrome_word or word == word[::-1]]
print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(palindrome_word)} times")