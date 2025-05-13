<template>
    <h1>ChildItem</h1>
    <P>{{ item.id }}</P>
    <P>{{ item.name }}</P>
    <!-- 버튼 클릭 시, someEvent 발생!!!! -->
    <!-- 이미 있는 기존 이벤트 이름을 쓰면 안됨..... -->
    <!-- <button @click="$emit('someEvent')">클릭</button> -->
    <button @click="buttonClick">클릭</button>
</template>

<script setup>
// 실제로 item에 대한 정보를 script 영역에서 사용하고 싶으면 
// defineProps 함수의 반환결과를 변수에 담아줘야 console.log로 찍어볼 수 o
// 절대, 하위 컴포넌트에서 prop 받은 데이터를 변경하기 위해 준 기능은 xxxxxxxx!!!!!!!!!
// props.item.name = '파인애플' 처럼 임의로 할당하면 의도와 달라짐.. 
// 객체 자체는 readonly..!
    const props = defineProps({
        item: Object,
    })
    // console.log(item) 안나옴 
    console.log(props) 
    console.log(props.item)
    const emit = defineEmits(['someEvent'])
    const buttonClick = function(){
        emit('someEvent', props.item, '구아바') // prop받은 item 정보를 넘겨줄 것
        // 해당 정보가 Child.vue의 const onSomeEvent 함수의 () 로 넘어갈 것

    }

</script>

<style scoped>

</style>