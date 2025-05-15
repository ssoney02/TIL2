import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // 사용자가 값을 CUD 할 때 반응할 수 있도록 반응형으로 작성
  let id = 0  // 애는 store내부에서만 사용할 일반 변수 -> 리턴 안해도 됨
  const todos = ref([
    // todo 객체 들을 만든다
    // input: checkbox에 쓰일 id도 필요하고, v-for로 순회할 때 쓸 key도 필요
    // 더미 데이터니까 1, 2, 3 할 수도 있는데,, 나주엥 값이 추가됐을 때도 처리!
    {id: id++, text: 'vue 공부', isDone: false},
    {id: id++, text: 'JS 공부', isDone: false},
    {id: id++, text: 'django 공부', isDone: true}

  ])

  const addTodo = function(todoText){
    todos.value.push({
      id: id++,
      isDone: false,
      text: todoText
    }) //상태 관리하는 영역이고 todos는 ref로 만들어져있으므로 value사용해야됨

  }
  const deleteTodo = function (selectedId){
    // 넘겨 받은 id 값을 기준으로
    // 내가 가진 todos를 전체 순회하면서, 각각의 todo 객체가 가진 id와 비교한다
    // 그리고, 비교한 결과가 true인 값을 반환할 떄의 todo만 모아서 새로운 배열을 만듦
    todos.value = todos.value.filter(todo => todo.id != selectedId)
  }

  const updateTodo = function(selectedId){
    todos.value = todos.value.map((todo) => {
      if (todo.id === selectedId) {
        todo.isDone = !todo.isDone
      }
      return todo // map 메서드 -> 바뀐 todo 반환해줘야됨
    })
  }
  return {
    // 값 선언 했으면, 바로바로 까먹지 않도록 return 해주자.
    // 상태 변수만 return 하기로 했음!!!!!!!!
    todos,
    addTodo, deleteTodo, updateTodo, 
  }
}, { persist: true})
