// store/articles.js
import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('article', () => {
  // 1.  axios 요청으로 api/v1/articles에 GET 요청을 보낼 함수 작성
  // 2. 그 게시글 조회 함수를 어디선가 요청을 보내야됨
  const articles = ref([
    {id: 1, title: 'title1', content:'content1'},
    {id: 2, title: 'title2', content:'content2'},
  ])
  const API_URL = 'http://127.0.0.1:8000'
  const getArticles = function(){
    // ArticleView 컴포넌트가 호출될 때 마운트!
    axios({
      method: 'GET',
      // 자주 요청 보내게 될 API_URL -> 변수로 관리하는게 좋음
      url: `${API_URL}/api/v1/articles/`  // 백틱!!!!
    })
    .then(res => {
      // console.log(res)
      // console.log(res.data) // Array
      articles.value = res.data
    })
    .catch(err => console.log(err))
  }
  return { 
    articles, API_URL, getArticles, 
  }
}, { persist: true })
