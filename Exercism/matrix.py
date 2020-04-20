class Matrix_Rows_Columns():
    def __init__(self, matrix_string):
        self.__matrix_rows = [[int(item) for item in row.split(' ')] for row in matrix_string.split('\n')]
        self.__matrix_columns = [list(column) for column in zip(*self.__matrix_rows)]

    def rows(self, big_list=[]):
        for item in range(len(self.__matrix_rows)):
            # print(self.__matrix_rows[item])
            for thing in self.__matrix_rows[item]:
                big_list.append(thing)
        print('rows: ', big_list)
        return big_list

    def columns(self, big_list=[]):
        for item in range(len(self.__matrix_columns)):
            # print(self.__matrix_columns[item])
            for thing in self.__matrix_columns[item]:
                big_list.append(thing)
        print('columns: ', big_list)
        return big_list



if __name__ == "__main__":
    input = '9 8 7\n5 3 2\n6 6 7'
    # add_rows(input)
    mat = Matrix_Rows_Columns(input)
    mat.rows()
    mat.columns()
