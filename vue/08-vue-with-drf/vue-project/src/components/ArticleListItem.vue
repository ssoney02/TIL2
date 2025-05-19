<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <!-- 디테일 페이지로 이동할 수 있는 링크를 만드는 방법 2가지 -->
     <!-- RouterLink or router.push -->
    <RouterLink :to="{name:'DetailView', params:{id: article.id}}">[Detail]</RouterLink>
    <hr>
  </div>
</template>

<script setup>
  const props = defineProps({
    article: Object,
  })
  import { RouterLink, } from 'vue-router'

</script>
