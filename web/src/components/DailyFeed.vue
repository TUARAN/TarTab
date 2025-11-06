<template>
  <div class="grid md:grid-cols-3 gap-4 mt-10 px-6">
    <div v-for="card in cards" :key="card.title" class="bg-gray-900 p-4 rounded-xl hover:bg-gray-800 transition">
      <h2 class="text-xl font-semibold mb-2">{{ card.title }}</h2>
      <p class="text-gray-400 text-sm mb-2">{{ card.desc }}</p>
      <a :href="card.link" target="_blank" class="text-neon text-sm hover:underline">查看详情 →</a>
    </div>
  </div>
</template>

<script setup>
const cards = [
  { title: 'DeepSeek-R1 模型', desc: '上下文压缩的新思路', link: 'https://huggingface.co/deepseek-ai' },
  { title: 'LangGraph 框架', desc: '构建多智能体工作流的核心', link: 'https://github.com/langchain-ai/langgraph' },
  { title: 'Claude 3.5 发布', desc: '多模态能力全面升级', link: 'https://www.anthropic.com' },
]
</script>

