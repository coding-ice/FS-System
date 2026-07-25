<template>
  <ul class="wrap" @click="handleClick">
    <template v-for="val in list" :key="val">
      <li :data-value="val" :class="{ [$style.grey]: selected === val }">{{ val }}</li>
    </template>
  </ul>
</template>
<script setup>
import { ref } from 'vue'

const selected = ref('1')

const list = ['1', '2', '3', '4', '5', '6']

const handleClick = (e) => {
  // 事件发生的元素
  const target = e.target
  if (target.tagName !== 'LI') return

  const value = target.dataset.value
  selected.value = value
}


</script>
<style module scoped>
.grey {
  background: var(--vp-custom-block-details-bg);
}

li {
  cursor: pointer;
}
</style>