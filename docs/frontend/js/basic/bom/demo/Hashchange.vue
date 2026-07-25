<template>
  <button @click="handleClick">change hash: ({{ count }})</button>
</template>
<script setup>
import { ref, onMounted } from 'vue'

const count = ref(0)

const handleClick = () => {
  location.hash = ++count.value
}

onMounted(() => {
  window.addEventListener('hashchange', function (e) {
    console.log('hash ->', decodeURIComponent(location.hash))
  })
})
</script>

<style scoped>
button {
  background: var(--vp-custom-block-details-bg);
  padding: 5px;
  border-radius: 5px;
}
</style>