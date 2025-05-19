<template>
  <div>
    <h1>Create page</h1>
    <form @submit.prevent="createArticle">
      <!-- input 태그, textarea가 비었을 떄 처리되도록 하는 로직 필요.. -->
      <label for="title">title: </label>
      <input type="text" id="title" v-model="title">
      <br>
      <label for="content">content: </label>
      <input type="text" id="content" v-model="content">

      <input type="submit" value="[CREATE]">
    </form>
  </div>
</template>

<script setup>
  // 1. axios
  import axios from 'axios'
  // 2. 게시글 상세조회 요청 경로: 출처가 이미 스토어에 있음
  import {useArticleStore} from '@/stores/articles.js'
  // 3. 응답 받은 게시글을 저장할 위치 : 반응성
  import { ref } from 'vue'
  // 4. 게시글 생성 완료 후 , router.push
  import { useRouter } from 'vue-router'  
  const title = ref(null)
  const content = ref(null)

  const store = useArticleStore()
  const router = useRouter()
  const createArticle = function(){
    axios({
      method:'post',
      url: `${store.API_URL}/api/v1/articles/`,
      data: {
        title: title.value,
        content: content.value
      }
    })
    .then(res => {
      console.log(res)
      console.log(res.data)
      // 정상적으로 응답이 왔으면 articleview로 이동
      router.push({name:'DetailView', params:{ id: res.data.id }})
    })
    .catch(err => console.log(err))
  }
</script>

<style>

</style>
