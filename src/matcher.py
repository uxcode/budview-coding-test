import math


class Person:
    def __init__(self, index: int, hobbies_bit: int):
        self.index = index
        self.hobbies_bit = hobbies_bit


class Matcher:
    MAXIMUM_MATCH = 10
    MAX_HOBBIES = 25
    BINARY = 2

    def __init__(self):
        self.couples = None
        self.max_matched = 0

    def get_couples(self, raw_people) -> list:
        self.couples = []
        self.max_matched = 0

        num_line = int(raw_people[0])

        people = []

        for i in range(num_line):
            index = i+1
            hobbies = raw_people[index]
            people.append(Person(index, self._convert_to_bit(hobbies)))

        people.sort(key=lambda person: person.hobbies_bit, reverse=True)

        for i in range(0, num_line - 1):
            person_a = people[i]
            person_b = people[i+1]
            num_matched = self._calculate_num_matches(person_a.hobbies_bit, person_b.hobbies_bit)
            self._update_couples(num_matched, person_a.index, person_b.index)

        for i in range(2, num_line):
            for j in range(i - 2, -1, -1):
                person_a = people[j]
                person_b = people[i]

                if self._determine_loop_break(person_a.hobbies_bit, person_b.hobbies_bit):
                    break

                num_matched = self._calculate_num_matches(person_a.hobbies_bit, person_b.hobbies_bit)
                self._update_couples(num_matched, person_a.index, person_b.index)

        self.couples.sort()
        return self.couples

    def _update_couples(self, num_matched, index_a: int, index_b: int) -> None:
        if num_matched > self.max_matched:
            self.couples = [self._get_formatted_couple(index_a, index_b)]
            self.max_matched = num_matched
        elif num_matched == self.max_matched:
            self.couples.append(self._get_formatted_couple(index_a, index_b))

    def _determine_loop_break(self, hobbies_a: int, hobbies_b: int) -> bool:
        if self._determine_loop_break_full_matched_case(hobbies_a, hobbies_b):
            return True
        else:
            return self._determine_loop_break_diff_bits_more_than_max_matched(hobbies_a, hobbies_b)

    def _determine_loop_break_full_matched_case(self, hobbies_a: int, hobbies_b: int) -> bool:
        if self.max_matched == self.MAXIMUM_MATCH:
            if hobbies_a - hobbies_b == 0:
                return False
            else:
                return True

    def _determine_loop_break_diff_bits_more_than_max_matched(self, hobbies_a: int, hobbies_b: int) -> bool:
        adjust_safe_diff = 2

        max_bit_place_b: int = self._get_max_bit_place(hobbies_b)
        rest_a_bit = hobbies_a >> max_bit_place_b + adjust_safe_diff
        count_rest_a = self._count_bits(rest_a_bit)

        if count_rest_a <= self.MAXIMUM_MATCH - self.max_matched:
            return False
        else:
            return True

    def _get_max_bit_place(self, value: int) -> int:
        for place in range(self.MAX_HOBBIES, 0, -1):
            if value & int(math.pow(self.BINARY, place)) > 0:
                return place

    def _convert_to_bit(self, hobbies: str) -> int:
        bit_hobbies = 0
        gap_between_hobby_chars = 2
        for j in range(0, len(hobbies), gap_between_hobby_chars):
            char = hobbies[j]
            bit_hobbies += int(math.pow(self.BINARY, ord(char) - ord('A')))
        return bit_hobbies

    def _calculate_num_matches(self, hobby_a: int, hobby_b: int) -> int:
        compare = hobby_a & hobby_b
        if compare > 1:
            return self._count_bits(compare)
        else:
            return 0

    @staticmethod
    def _count_bits(n) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

    @staticmethod
    def _get_formatted_couple(index_a: int, index_b: int) -> str:
        return '{}-{}'.format(min(index_a, index_b), max(index_a, index_b))
