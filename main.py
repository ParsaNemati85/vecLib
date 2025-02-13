import warnings
import vectors

warnings.filterwarnings('error')


def main():
    question_v = {"a":5, "b":9}
    abs_v = vectors.StringVectors([{"a":1, "b": 2},{"a":3, "b": 4, "c":5}, {"a":6, "b": 7, "c": 8, "d": 9}, {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}, question_v])

    v_list = abs_v.get_list_as_vectors()
    angle_list = []
    for i in range(len(abs_v.get_list_as_vectors())):
        angle_list.append(v_list[i].get_angle(v_list[len(v_list) - 1]))

    print(angle_list)

    return 0

if __name__ == "__main__":
    main()