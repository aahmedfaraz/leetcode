class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combs = []

        def add_combination(prev_comb: str, new_char: str, opening: int, closing: int):
            if opening < closing or opening > n or closing > n: return
            new_comb = prev_comb + new_char
            if opening == closing and opening == n:
                combs.append(new_comb)
            add_combination(new_comb, "(", opening + 1, closing)
            add_combination(new_comb, ")", opening, closing + 1)

        add_combination("", "(", 1, 0)
        add_combination("", ")", 0, 1)

        return combs

# time complexity = 