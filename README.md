# img2ascii                                                                          

###结构说明
img2ascii.py 负责转换
run.py 封装命令行工具
dist内是使用py2exe工具打包的win可执行程序

###使用说明


在命令行下打开
python run.py 或者
img2ascii.exe -h 查看帮助
使用示例：

img2ascii.exe sample.jpg 输出至sample.jpg.txt，请在等宽字体下查看。

img2ascii.exe sample.jpg  -r 0.3 将输出缩放至30%输出至sample.jpg.txt，