<template>
  <div :class="$style.btns">
    <template v-for="val in wrapValues" key="val">
      <button :class="{ [$style.active]: wrap === val }" @click="wrap = val">{{ val }}</button>
    </template>
  </div>
  <div :class="[$style.container, $style[wrap]]">
    <div>1</div>
    <div>2</div>
    <div>3</div>
    <div>4</div>
    <div>5</div>
    <div>6</div>
    <div>7</div>
    <div>8</div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import { wrapValues } from './config.ts'


const wrap = ref(wrapValues[0]);
</script>
<style module>
@import url("./common.css");
</style>
