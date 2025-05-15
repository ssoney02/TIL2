<template>
<div>
    <!-- store.addTodo(todoText) -> 이렇게 써도 됨! 그치만.. 그렇게 안할것.. 별도의 함수 따로 정의해서 작성할것  -->
    
    <form @submit.prevent="onAddTodo">

        <!-- 양 방향 바인딩으로, 사용자가 입력한 값을 사용하자. -->
        <input type="text" v-model="todoText">
        <button>Create</button>
    </form>
</div>
</template>

<script setup>    
    import { ref } from 'vue'
    import {useCounterStore} from '@/stores/counter.js'
    const store = useCounterStore()
    const todoText = ref('')
    // store에 있는 addTodo -> todos.value에 객체를 push하는 역할
    // TodoForm에서 submit 됐을 때 실행할 함수 -> todoForm을 위한 todoText를 다시 빈문자열로 초기화해야됨 
    //      -> store에 있는 addTodo가 할 일은 xx
    //          그래서 onAddTodo함수 다시 정의할 것... (함수하나 - 기능 하나)
    const onAddTodo = function(){
        store.addTodo(todoText.value)
        todoText.value = ''
    }

</script>

<style scoped>

</style>