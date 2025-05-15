<template>
<div>
  <!-- <p>state: {{ store.count }}</p>
  <p>getters: {{ store.doubleCount }}</p>
  <button @click="store.increment">click</button> -->
  <!-- <hr>
  <Example /> -->
  <h1>Todo Project</h1>
  <TodoList />
  <TodoForm />
</div>
</template>

<script setup>
  // import Example from './components/Example.vue'
  import TodoForm from '@/components/TodoForm.vue'
  import TodoList from '@/components/TodoList.vue'
  import { useCounterStore } from './stores/counter.js'
  const store = useCounterStore()
  console.log(store)
  
</script>

<style scoped>

</style>