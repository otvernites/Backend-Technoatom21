from exception import NotListError


class CustomList(list):

    def check_type(self, curr_list):
        if not isinstance(curr_list, (CustomList, list)):
            raise NotListError

    def __rsub__(self, curr_list):
        lst = self - curr_list
        for i in enumerate(lst):
            lst[i[0]] = i[1] * (-1)
        return lst

    def __sub__(self, curr_list):
        self.check_type(curr_list)
        result = CustomList()
        min_len = min(len(self), len(curr_list))
        [result.append(self[i] - curr_list[i]) for i in range(min_len)]
        if len(self) != len(curr_list):
            if min_len == len(self):
                while min_len != len(curr_list):
                    result.append((-1) * curr_list[min_len])
                    min_len += 1
            else:
                while min_len != len(self):
                    result.append(self[min_len])
                    min_len += 1
        return result

    # a+b = a-(-1*b)
    def __add__(self, curr_list):
        self.check_type(curr_list)
        for i in enumerate(curr_list):
            curr_list[i[0]] = i[1] * (-1)
            result = self - curr_list
            return result

    def __eq__(self, curr_list):  # ==
        self.check_type(curr_list)
        return sum(self) == sum(curr_list)

    def __ne__(self, curr_list): # !=
        self.check_type(curr_list)
        return not self.__eq__(curr_list)

    def __lt__(self, curr_list):  # <
        self.check_type(curr_list)
        return sum(self) < sum(curr_list)

    def __ge__(self, curr_list):  # >=
        self.check_type(curr_list)
        return not self.__lt__(curr_list)

    def __gt__(self, curr_list):  # >
        self.check_type(curr_list)
        return sum(self) > sum(curr_list)

    def __le__(self, curr_list):  # <=
        return not self.__gt__(curr_list)
