<template>
    <h1>Parent</h1>
    <p>{{ userName }}</p>
    <!-- parent-name -> 문자열을 할당하기 위한 속성.... -->
    <Child 
        :user-name="userName"
        parent-name="Bella"
        @change-user-name="$emit('changeUserName')"
    />
</template>

<script setup>
    import Child from './Child.vue'
    // prop 정보를 정의하는 방법은 여러가지
    defineProps({
        // HTML 속성은 케밥케이스지만,
        // JS 변수명은 카멜케이스가 기본
        userName: String  // type을 지정해줘야됨....
        // 기본값을 지정하거나, 유효성을 검사하는 등.. 추가 옵션 활용하려면 아래 처럼 적어야됨...
        // userName: {
        //  type: String,
        //  required: true
        //}
    })
</script>

<style scoped>

</style>