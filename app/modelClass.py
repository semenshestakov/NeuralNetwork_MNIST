from tensorflow.keras.models import load_model
from numpy import array, argmax
from os import listdir


class Model:
    def __init__(self, path=None):

        self.update_model_path(path)
        self.pool = load_model("Models/Pool")

    def update_model_path(self, new_path: str):
        self.search()
        if new_path in self.models:
            self.model = load_model(new_path)
            self.path = new_path
        elif new_path is None:
            self.model = load_model(self.models[0])
            self.path = self.models[0]

        else:
            raise ValueError(
                f"Не найден файл {new_path} в ближайшем окружении\n" +
                f"File {new_path} not found in immediate environment"
            )

    def __call__(self, imag: array, fl_print: bool = False, fl_imgs: bool = False) -> array:
        """

        :param imag: np.array ,shape = (448,448)
        :param fl_imgs : bool если True то мы imag используем как готовый вариат (1,28,28,1)

        :param fl_print:
            if fl_print:
                n = np.argmax(self.result_models)
                print(f"Result: {n}\nConfidence:{self.result_models[0][n]}")

        :return:result models : np.array, shape = (1,10)
        """
        if fl_imgs is False:
            imag.shape = (1, 448, 448, 1)
            imag = array(self.pool(imag))

        self.result_models = self.model(imag)
        if fl_print:
            n = argmax(self.result_models)
            print(f"Result: {n}\nConfidence:{self.result_models[0][n]}")

        return self.result_models, imag

    def search(self, fl_return: bool = False):

        """
        Функция ищет все файлы с названием "Model"
        и записывает все подходящие файлы в переменую self.models : [str]
        :param fl_return
            if fl_return is True:
                :return: List[str] models
            else:
                :return None
        """
        # print(listdir(path="./Models"))
        self.models = ["./Models/" + i for i in listdir(path="./Models") if "Model" in i]

        return self.models if fl_return is True else None

    def __len__(self):
        return len(self.models)

    def __str__(self):
        return self.path
