<template>
  <div>
    <h1>Article page</h1>
    <ArticleList />
    <RouterLink :to="{name: 'CreateView'}">[Create]</RouterLink>
  </div>
</template>

<script setup>
  import ArticleList from '@/components/ArticleList.vue'
  import { useArticleStore } from '@/stores/articles.js'
  import { onMounted } from 'vue'
  import { RouterLink } from'vue-router'
  const store = useArticleStore()
  // 이 컴포넌트가 mount될 때 전체 게시글 조회
  // onMounted 함수가 실행되었을 때, 다른 함수를 실행하고 싶음 => 콜백함수 정의
  onMounted(()=>{
    store.getArticles()

  })
</script>

<style>

</style>
