# NeuralNetwork MNIST

Программа для визуализации работы сети на своих данных, краткое введение в Deep Learning. Решение задания на Kaggle. И  нейросеть для генирации цифр по лейблу (GAN)

Всё что касаемо обучения моделей находится в директории "CreateNetwork" \
В ноутбуке analytics находиться пример моего мышления, как можно увеличить базу данных в несколько раз, можно правда еше в 4 раза ее увеличить, если поворачивать данные на 90 градусов. \
extensionbase.py - реализация идеи по увеличению базы данных.\
keras_CNN/(Dense) - код и объяснения что, зачем и как мы делаем, чтобы обучить модель.

В Models находиться разной сложностью модели для тестирования
Файлы которые начинаются на "Model" - это примеры обученых сетей, "ep" - эпохи, "ex" - обучена на увеличенной базе данных.
"Pool" - это 1 слой AvgPool, который сжимает 448х448 до 28х28

# app - Программа для визуализации 
main - это файл от куда запускается программа, Menu/modelClass - это вспомогательные модули для main
https://disk.yandex.ru/d/5XWjU-mfO_JPlQ - ссылка на exe файл этой программы.
Вся информация как пользоваться программой представлена в файле "Руководство по программе"

<img width="450" alt="Screenshot 2023-06-22 at 19 35 03" src="https://github.com/posyd0moika/NeuralNetwork_MNIST/assets/94396766/3e3977db-a3b3-4a0a-aa39-b191bb58460c">
<img width="450" alt="Screenshot 2023-06-22 at 19 35 11" src="https://github.com/posyd0moika/NeuralNetwork_MNIST/assets/94396766/911f5f94-fc81-4b35-9784-42ea34f6b769">


## Kaggle
Kaggle - в это директории, есть дополнительная обучающая выборка, а также пример что нужно записать в данные для участия в соревнованиях Kaggle (https://www.kaggle.com/competitions/digit-recognizer/overview)\
"for kaggle" - код как я работал с базой данных, записывал данные.
В начале у меня результат показал Kaggle не очень хороший. Я решил до-обучить сеть на данных взятых на соревнованиях. И я попал в топ 22%(занял 356 место с точностью 0.99192), за 10 минут результат неплохой.


## GAN
Наверное самое сложное и одновременно самое интересное - это GAN (Generative adversarial network / генеративно-состязательные сети)
Первое что я реализовал - это генерация изображений с одинаковым лейблом, это было сделано для того чтобы понять вообще работает моя архитектура для генерации и не напутал ли я в обучении. 
Потом я экспериментировал с архитектурой НС, где были реализованы «skip connection», как в генераторе так и в дискриминатор, также пришел к выводу, что MSE работает лучше чем BinaryCrossentropy. /
Обучал я в Colab и сохранял промежуточные результаты себе на диск. 

#### Гипотеза 1.

В архитектуре сети я объединяю слои которые несут в себе класс объекта и шум. Гипотеза состоит в том что в определение класса для генерации цифры зависит от пропорции шума и класса объекта. 
Если вектор шума больше чем класса, то изображения будут размазаны или не будет соответствие классу генерации. А если шума почти не будет, а будет вектор класса, то будет маленькое разнообразие цифр. 

В видео использовал один и тоже шум и одни и те же лейблы

https://github.com/semenshestakov/NeuralNetwork_MNIST/assets/94396766/b9d9e722-c6d4-411d-8091-3f296fb9e104
 
#### Гипотеза 1 подтвердилась.



