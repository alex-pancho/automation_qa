class MyMethods:
    def addit(a: int, b: int) -> int:
        """Add two variables"""
        addit_result = a + b

        return addit_result

    def list_avg(nums_of_list: list) -> int:
        """Calculate sum of all numbers and calculate average"""
        total_sum = sum(nums_of_list)
        avg = total_sum / len(nums_of_list)

        return avg

    def revers_string(str_rev: str) -> str:
        """Make type reversed and return type string"""
        str_r = reversed(str_rev)
        reversed_str = ''.join(str_r)

        return reversed_str

    def sum_of_input_digits() -> int:
        """The method returns sum of entered digits"""
        dig = input("Add digit: ")
        sum_num = 0
        if not dig.isdigit():
            return ("Enter digit!!!")
        elif int(dig) == 0:
            return ("Digit must be above 0!")
        else:
            for i in dig:
                sum_num = sum_num + int(i)
        return sum_num