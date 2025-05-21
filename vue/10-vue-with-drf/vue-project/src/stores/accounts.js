// store/accounts.js

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const ACCOUNT_API_URL = 'http://127.0.0.1:8000/accounts'
  const token = ref('')
  const isLogin = computed(() => {
    return token.value ? true : false
  })
  // signUp함수는 어떤 객체 정보 하나를 받아올 것
  const signUp = function(payload){
    console.log(payload)
    // const username = ref(payload.username)
    // const {username, password1, password2} = payload
    
    axios({
      method: 'post',
      url: `${ACCOUNT_API_URL}/signup/`,
      // data: { ...payload }
      data: payload,
    })
    .then(res => {
      console.log('성공~')
    })
    .catch(err =>{
      console.log(err)
    })
  }
  const logIn = function({username, password}){
    axios({
      method: 'post',
      url: `${ACCOUNT_API_URL}/login/`,
      data: {
        username, password,
      }
    })
    .then(res =>{
      token.value = res.data.key
      console.log('로그인완!')
    })
    .catch(err => {
      console.log(err)
    })
  }
  return { signUp, logIn, token, isLogin  }
}, { persist: true })
