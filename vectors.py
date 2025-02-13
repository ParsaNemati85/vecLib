import math

from qtconsole.rich_text import export_xhtml


class Vector(object):
    def __init__(self, components: list[float]):
        self.components = components

    def get_magnitude(self) -> float:
        """
        Returns the magnitude of the vector.
        :return:
        """
        magnitude = 0
        for component in self.components:
            magnitude += component**2

        return magnitude**0.5

    def get_angle(self, other) -> float:
        """
        Returns the angle of the vector
        with respect to another vector object.
        :return:
        """
        v1 = self.get_magnitude()
        v2 = other.get_magnitude()

        dot_product = 0
        for i in range(len(self.components)):
            dot_product += self.components[i] * other.components[i]
        return math.acos(dot_product/(v1*v2))





class StringVectors:
    def __init__(self, components: list[dict[str, int]]):
        """
        takes a list of dictionary of words
        the dictionary is in the format:
        <String: words, Float: number of times the word is said>
        :param components:
        """
        #english temp property
        self.english_tempelate = {}


        #find the largest dictionary:
        current_max_index = 0
        for dicts in range(len(components)):
            if len(components[dicts]) > len(components[current_max_index]):
                current_max_index = dicts

        #largest dictionary will serve as "english template"
        for keys in components[current_max_index]:
            self.english_tempelate.update({keys:0})

        #create a new list with all the numbers!
        self.refined_vector_list = []

        for dicts_ in components:
            #dicts are dictionaries in original data
            temp_dict = self.english_tempelate.copy()
            for keys_temp in temp_dict.keys():
                try:
                    temp_dict.update({keys_temp:dicts_[keys_temp]})
                except KeyError:
                    continue

            temp_list = []
            for value_ in temp_dict.values():
                temp_list.append(value_)
            self.refined_vector_list.append(temp_list)

    def get_list_as_vectors(self) -> list[Vector]:
        r_l = []
        for i in self.refined_vector_list:
            r_l.append(Vector(i))
        return r_l

