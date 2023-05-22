# AudioDiffGAN

#### Автор: Аксёнов Ярослав Олегович

## О модели
AudioDiffGAN - модель для быстрой необусловленной генерации человеческой речи, совмещающая в себе использование диффузии и генеративно состязательной сети для выполнения шагов расшумления. Отличительные особенности модели - это высокая скорость генерации, в 200 раз превышающая скорость генерации необусловленного DiffWave, при этом выдавая лучшее качество в терминах Mean Opinion Score, и сравнимое с DiffWave высокое разнообразие в генерируемых сэмплах. Ключевой идеей, позволяющей ускорить генерацию по сравнению с другими диффузионными моделями, является использование больших шагов в обратном диффузионном процессе с помощью генеративно состязательной сети, способной предсказывать мультимодальное распределение расшумления, а не нормальное распределение, как в обычных диффузионных моделях. Модель генерирует мел-спектрограмму, после чего она подается на вход быстрому вокодеру HiFiGAN, который выдает итоговый аудиофайл. В наших экспериментах мы обучали модель на датасете Speech Commands 09.

<image src="images/train_process.png" alt="Процесс обучения модели" width=70%>

## Графики функции потерь
Для модели с 2 шагами диффузии:

<image src="images/2step_loss.png" alt="График функции потерь для 2 шагов диффузии" width=70%>

Для модели с 4 шагами диффузии:

<image src="images/4step_loss.png" alt="График функции потерь для 4 шагов диффузии" width=70%>

## Метрики
<image src="images/metrics.png" alt="Метрики" width=100%>

## Примеры генерации мел-спектрограмм

### Для модели с 2 шагами диффузии:

После 360 эпох обучения:
<image src="mel_examples/mel_sample_2steps360.png" alt="2 steps 360 training steps">
После 500 эпох обучения:
<image src="mel_examples/mel_sample_2steps500.png" alt="2 steps 500 training steps">

### Для модели с 4 шагами диффузии:

После 400 эпох обучения:
<image src="mel_examples/mel_sample_4steps400.png" alt="4 steps 400 training steps">
После 500 эпох обучения:
<image src="mel_examples/mel_sample_4steps500.png" alt="4 steps 500 training steps">

## Примеры генерации аудио
  
(Корректно проигрывается через Google Chrome)
  
### Для модели с 2 шагами диффузии:

После 360 эпох обучения:

[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/6843ccef-8771-483f-83f3-88a2c403a241)
  
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/9be62811-7869-48b9-81c4-0898afe986c3)
  
Пример плохой генерации:
  
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/0689c428-575e-4b4b-9018-8c2ca01cd7ea)
  
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/117801e8-dfaf-4c8b-8b8c-2534d58e6f46)
  
После 500 эпох обучения:

[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/1dfb5860-2870-4cee-b4c5-19d640fc20ac)
  
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/47739440-1782-4db0-ad89-4d81e9137250)
  
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/6a1ab399-f26c-41c0-975b-6c49da2598bc)
  
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/26f4d60e-1d36-46c3-83c9-58f6ff11c913)

### Для модели с 4 шагами диффузии:
  
После 400 эпох обучения:

[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/a679d297-c87b-4f02-a329-f53d92a06fcf)
  
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/0944ab1d-b72c-4654-a6c0-1b4d110543b4)
  
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/e7310b33-3c5d-4a5f-9978-1cec18a2f305)
  
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/b7b9265e-7538-4d05-a9d2-21fb14127762)

После 500 эпох обучения:

[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/99176a55-e9ad-41ba-bc3c-cf502bfcaee7)
  
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/0fa4bc4b-5b3a-480b-8439-e789617f2fe1)
  
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/94717d0c-24d1-4e95-951c-56b4e74dfa42)
  
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/327edcbb-2d01-4733-8817-d5e86b3e5188)

### Запуск

Для запуска процесса обучения через bash запустить файл [audiodiffgan_train.sh](model/audiodiffgan_train.sh)

Для запуска процесса генерации через bash запустить файл [audiodiffgan_test.sh](model/audiodiffgan_test.sh)

