“案例二AI制图训练结果”文件夹里包含我训练得到的参数文件 generator_weight，
可直接用于生成图片。

images 文件夹里的是训练所用的图片。

=======
训练：

运行 python train.py 即可开始训练。

默认训练 100 个 Epoch，你可以提早结束训练（Ctrl + C）。

=======
生成图片：

训练完很多个 Epoch （训练几个 Epoch 是不够的，图片比较模糊）之后，
运行 python generate.py 即可生成图片。

如果等不了那么久，可以用我提供在“案例二AI制图训练结果”文件夹里的参数文件。
使 generator_weight 参数文件位于 generate.py 同级目录下，
运行 python generate.py 即可生成图片。
