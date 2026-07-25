<template>
  <div :class="$style.btns">
    <template v-for="dir in directionValues" key="dir">
      <button :class="{ [$style.active]: dir === direction }" @click="direction = dir">{{ dir }}</button>
    </template>
  </div>
  <div :class="[$style[direction], $style.container]">
    <div class="box">1</div>
    <div class="box">2</div>
    <div class="box">3</div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { directionValues } from './config.ts';

const direction = ref(directionValues[0]);

</script>

<style module>
@import url("./common.css");
</style>