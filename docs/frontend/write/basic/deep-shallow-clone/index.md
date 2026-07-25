# 深浅拷贝 （Deep/Shallow Clone）

## 浅拷贝 Shallow Clone

浅拷贝是指：**创建一个新对象，这个对象对于基本数据类型直接复制其值，对于引用类型复制其内存地址（引用）。**

<<< ./code/shallowClone.js

## 深拷贝 Deep Clone

深拷贝是指：**完全复制一个对象，包括对象中的嵌套对象，创建一个与原对象完全独立的新对象，两者不共享任何内存地址。**

<<< ./code/deepClone.js
