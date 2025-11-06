<template>
  <section class="h-screen flex flex-col justify-center items-center text-center">
    <h1 class="text-5xl font-bold mb-4">TarTab</h1>
    <p class="text-gray-400 mb-8">Tab Your Mind — 打开标签页，点亮你的思维</p>
    <input
      v-model="query"
      placeholder="搜索 GitHub / AI 工具 / 资讯"
      class="w-96 p-3 rounded-lg bg-gray-800 focus:outline-none"
    />
  </section>
</template>

<script setup>
import { ref } from 'vue'
const query = ref('')
</script>

