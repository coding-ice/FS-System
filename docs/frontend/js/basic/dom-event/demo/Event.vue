<template>
  <div :class="$style.container" @click="handleClick">
    <div :class="$style.box"></div>
  </div>
</template>
<script setup>
const handleClick = (e) => {
  console.log('target', e.target) // 1. 事件发生的元素
  console.log('currentTarget', e.currentTarget) // 2. 事件绑定的元素

  console.log('offsetX', e.offsetX) // 3. 元素内部的 x 坐标 padding起点
  console.log('offsetY', e.offsetY) // 4. 元素内部的 Y 坐标

  console.log('clientX', e.clientX) // 5. 触发点相对于浏览器窗口的 x 坐标
  console.log('clientY', e.clientY) // 6. 触发点相对于浏览器窗口的 y 坐标

  console.log('pageX', e.pageX) // 7. 触发点相对于整个文档的 x 坐标
  console.log('pageY', e.pageY) // 8. 触发点相对于整个文档的 Y 坐标

  console.log('screenX', e.screenX) // 9. 触发点相对于整个屏幕的 x 坐标
  console.log('screenY', e.screenY) // 10. 触发点相对于整个屏幕的 y 坐标
}
</script>
<style module>
.container {
  margin-top: 10px;
  width: 100px;
  height: 100px;
  background: skyblue;
  border: 5px solid purple;
  padding: 5px;

  .box {
    width: 50px;
    height: 50px;
    background: pink;
  }
}
</style>