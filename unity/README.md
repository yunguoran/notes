# Unity

从 0 编程制作类银河恶魔城游戏 in Unity6 [bilibili 视频教程](https://www.bilibili.com/video/BV1Zs3gzKEDP/)，正版教程见 [Udemy](https://www.udemy.com/course/2d-rpg-alexdev/)。

- Editor -> Preferences -> External Tools -> External Script Editor 可以关联 Visual Studio。
    - 关联之后需要点击 Regenerate project files。
- Editor -> Project Settings -> Input Manager 有预设按键，例如：Jump 为 KeyCode.Space。

## Hierarchy

## Scene

- 双击 Hierarchy 中的元素，会聚焦到该元素。
- 按下鼠标中键，可以在任意工具模式切换到 View Tool 工具用以拖动场景。
- Scale Tool 改变的是物体的缩放比例（[Transform.localScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localScale.html)），Unity 渲染的时候会把原始数据乘上缩放比例，再显示出来。
    - 缩放比例就是一个乘法系数。
    - 这样既能等比缩放（所有轴同一个系数），也能非等比缩放（各轴不同系数）。
    - 因此 Scale Tool 并不改变
- 工具栏工具的排列顺序和键盘第一列排列互相映射，比如 Q 会选中 View Tool。
    - 123
    - 456

## Shortcuts

Ctrl + d 快速复制
Ctrl + p 快速 play
Ctrl + Shift + c 打开控制台

## Inspector

双击 Script 可以打开脚本。

## Component

### Rigidbody

Rigidbody 2D 有 Gravity Scale 属性，默认为 1，因此会下落。

### Physics Material

Physics Material 有 Friction 和 Bounciness 两个属性。
