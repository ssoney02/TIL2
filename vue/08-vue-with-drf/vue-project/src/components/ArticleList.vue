<template>
  <div>
    <h3>Article List</h3>
    <ArticleListItem v-for="article in store.articles"
    :key="article.id"
    :article="article"/>
    <!-- 하위 컴포넌트에서 데이터 사용할 수 있도록 prop -->
  </div>
</template>

<script setup>
import ArticleListItem from '@/components/ArticleListItem.vue'
import { useArticleStore } from '@/stores/articles.js'
const store = useArticleStore()

</script>
