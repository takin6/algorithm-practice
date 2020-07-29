def letter_combinations(digits):
    d_map = { "2": ["a", "b", "c"],
      "3": ["d", "e", "f"],
      "4": ["g", "h", "i"],
      "5": ["j", "k", "l"],
      "6": ["m", "n", "o"],
      "7": ["p", "q", "r", "s"],
      "8": ["t", "u", "v"],
      "9": ["w", "x", "y", "z"]}

    def make_comb(comb, rem_digits):
        if len(rem_digits) == 0:
            ans.append(comb)
            return
        else:
            for char in d_map[rem_digits[0]]:
                make_comb(comb+char, rem_digits[1:])

    ans = []
    make_comb("", digits)

    return ans

print(letter_combinations("23"))