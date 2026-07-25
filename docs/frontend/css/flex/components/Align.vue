<template>
  <div :class="$style.btns">
    <template v-for="dir in directionValues" key="dir">
      <button :class="{ [$style.active]: dir === direction }" @click="direction = dir">{{ dir }}</button>
    </template>
  </div>

  <div :class="$style.btns">
    <template v-for="val in alignValues" key="val">
      <button :class="{ [$style.active]: align === val }" @click="align = val">{{ val }}</button>
    </template>
  </div>
  <div :class="[$style.container, $style[`align-${align}`], $style[direction]]">
    <div>1</div>
    <div>2</div>
    <div>3</div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { alignValues, directionValues } from './config.ts'

const align = ref(alignValues[0]);
const direction = ref(directionValues[0]);

</script>
<style module>
@import url("./common.css");

.container {
  height: 200px;

  div {
    height: auto !important;
  }
}
</style>
