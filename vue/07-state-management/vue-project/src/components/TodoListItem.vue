<template>
<div>
    <!-- 속성에 넣는 것과 template syntax 작성방법 다른 것 헷갈리지 말기!!!!!! 속성 -> bind!!!!!!!!!-->
     <!-- 양방향 binding -> 체크하면 isDone이 true가 되도록 -->
      <!-- isDone에 대한 값은 counter.js에서 관리해야됨!!!! -> 여기서 직접 변경하진 않을 것임... -->
    <input type="checkbox" :id="todo.id" v-model="isDone">
    <!-- 
        label의 for와 같은 값을 가진 id를 찾아서  
        label에 작성된 textContent를 click하면
        찾아둔 동일 id를 가진 요소에 focus
    -->
    <label :for="todo.id">{{ todo.text }}</label>
    <button @click="onDeleteTodo">삭제</button>
</div>
</template>

<script setup>
    import { useCounterStore } from '@/stores/counter.js'
    import { ref, watch } from 'vue'
    const props = defineProps({
        todo: Object,
    })
    

    const store = useCounterStore()
    
    // prop받은 원본 데이터를 일단 화면에 표시! -> v-model로 양방향 바인딩
    const isDone = ref(props.todo.isDone)
    // isDone이 변경되면 update함수를 호출 할 것!
    //  -> watch로 isDone을 감시하고 있다가, 변경이 되면 store가 가진 updateTodo를 호출
    watch(isDone, () => {
        store.updateTodo(props.todo.id)
    })

    const onDeleteTodo = function(){
        store.deleteTodo(props.todo.id)
    }
</script>

<style scoped>

</style>