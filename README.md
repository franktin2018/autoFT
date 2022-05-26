# autoFT

## Auto Facial Test

输入规范：文件序列格式
 * 文件路径/名称.$F.obj
    * $F 表示 frame 号码，当前在第几帧，是一个int
    * $F4 表示 对 frame 数值进行格式化
        * $F  : 1,2,3,4 ...
        * $F4 : 0001,0002,0003,0004 ...
        * $F5 : 00001,00002,00003,00004 ...
* Example:
    * E:/liewi/Input/head.$F4.obj 

----

## Python Example

``` python
import os

#设置 hython 路径
# hython 是houdini 的 python 命令运行环境，可以用python 控制 houdini
# hython 在Houdini 安装路径下 bin 文件夹里
hythonPath ="\"C:/Program Files/Side Effects Software/Houdini 18.5.672/bin/hython.exe\""

#要Houdini去执行的Python脚本
executePython = "E:/MTStudio/lilwei/runTemplate.py"

#要执行的hip文件
hipFile = "E:/MTStudio/lilwei/Template.hip"

#命令行启动 hython，hython 后面的其实都是命令行参数
os.system(hythonPath + " " + executePython + " " + hipFile)

```

----


## Json config 字段解释


``` json
{
    "TaskType":0,                               // 0 是 输出法线圆滑模型，1 是渲染出图，2是both
    "ObjSrc":"E:/MTStudio/lilwei/geo/modelA/",  //obj 序列路径
    "ObjFileName":"head.$F.obj",                //obj 文件名
    "ObjTex":"E:/MTStudio/lilwei/.../00000.png",//texture 数字人的脸部纹理贴图
    "UseSubdivide":1,                           //是否开启subdivide 细分
    "OutObj":"E:/MTStudio/lilwei/geo/name.$F4.obj",
    "OutPic":"E:/MTStudio/lilwei/pic/name.$F4.jpg",
    "Res":[512,512],                            //渲染的分辨率大小
    "RenderRange":[1,300],                      // 需要输出的 帧数范围
    "Samples":[2,2]                             //渲染的采样精度，数值越大，噪点越少，速度越慢
}

```

