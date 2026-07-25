<template>
  <div :class="$style.btns">
    <template v-for="dir in directionValues" key="dir">
      <button :class="{ [$style.active]: dir === direction }" @click="direction = dir">{{ dir }}</button>
    </template>
  </div>

  <div :class="$style.btns">
    <template v-for="val in justifyContentValues" key="val">
      <button :class="{ [$style.active]: val === justify }" @click="justify = val">{{ val }}</button>
    </template>
  </div>
  <div :class="[$style.container, `${$style[`justify-${justify}`]}`, $style[direction]]">
    <div>1</div>
    <div>2</div>
    <div>3</div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { justifyContentValues, directionValues } from './config.ts'

const justify = ref(justifyContentValues[0]);
const direction = ref(directionValues[0]);

</script>
<style module>
@import url("./common.css");
</style>
