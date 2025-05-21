<!-- views/LoginView.vue -->

<template>
  <div>
    <form @submit.prevent="onLogIn">
      <label for="username">username: </label>
      <input type="text" id="username" v-model="username">
      <br>
      <label for="password">password: </label>
      <input type="text" id="password" v-model="password">
      <br>
      <button type="submit">login</button>
    </form>
  </div>
</template>

<script setup>
  import {ref } from 'vue'
  import { useAccountStore } from '@/stores/accounts';
  const accountStore = useAccountStore()
  const username = ref(null)
  const password = ref(null)

  const onLogIn = function(){
    const userInfo = {
      username: username.value,
      password: password.value,
    }
    accountStore.logIn(userInfo)
  }
</script>

<style>

</style>
