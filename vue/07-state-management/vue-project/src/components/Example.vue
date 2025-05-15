<template>
<div>
    <h1>example</h1>
    <p>state: {{ store.count }}</p> 
    <p>getters: {{ store.doubleCount }}</p>   
    <button @click="store.increment">click</button>
</div>
</template>

<script setup>
  import { useCounterStore } from '../stores/counter.js'
  const store = useCounterStore()
</script>

<style scoped>

</style>