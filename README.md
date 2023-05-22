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
  
### Для модели с 2 шагами диффузии:

После 360 эпох обучения:

[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/d510f4fd-c5c0-43ba-8bc3-2df33b59ac38)
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/d9ca3f4a-0bb6-453b-9e1d-cf5d908ab786)
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/f15acdce-46da-4063-b51f-d052c19cefee)
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/d5e2200d-cf75-489f-b184-8327c438e37a)
  
После 500 эпох обучения:

[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/4cf3ab1a-6a6f-43a2-bbc2-685af341363b)
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/f7ea11ff-87a7-4d87-8da1-f4a73ef826cc)
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/b14eaea0-da1e-43f0-95fc-95090bc8904b)
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/47b40552-57d7-4ae4-a229-ba211d364236)


### Для модели с 4 шагами диффузии:
  
После 400 эпох обучения:

[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/74086c91-c0bb-4a5b-8c8e-7609a623d9f6)
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/e0607d1b-1630-406a-8eff-f7af7c47117e)
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/ab937cb4-0f34-4a74-9274-2d835bb60ed8)
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/e4507b0e-9e35-4d5e-a72c-dfdc928b00c5)


После 500 эпох обучения:

[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/d8d10a15-3d5b-4702-9a42-91b57a0648cb)
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/cc96e0d3-55cb-4132-9b69-b1ac68fb2602)
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/f44ecdcc-b9ff-42e5-a5fe-cea17841e09c)
[Audio](https://github.com/yaraksen/AudioDiffGAN/assets/26881591/a7b9e664-f570-409b-966e-e1b8e0926c98)
