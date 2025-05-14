<template>
    <div>
        <h1>User PAGE</h1>
        <button @click="goHome">Home!</button>
        <h2>현재 경로에 관련된 어떤 정보들은 {{ $route.params }}</h2>
        <h2>현재 경로에 관련된 어떤 정보들은 {{ $route.params.id }}</h2>
    <!-- post 혹은 profile로 이동할 수 있어야 함 -> link가 필요 -->
        <RouterLink :to="{name:'user-profile'}">Profile</RouterLink>
        <RouterLink :to="{name: 'user-post'}">Posts</RouterLink>
        <!-- 중첩된 자식들의 정보를 보여주고 싶음 -->
        <RouterView />
        
    </div>
</template>

<script setup>
// route기능 -> 우리가 프로젝트에 추가한 vue-router가 가지고 있음
import {useRoute, useRouter, RouterView, RouterLink, onBeforeRouteLeave} from 'vue-router'

    const route = useRoute()
    const router = useRouter()
    console.log(route)
    console.log(router)
    const goHome = function(){
        // 어디로 이동?
        router.push({name:'home'})
    }
    onBeforeRouteLeave((to,from) => {
        const answer = window.confirm('정말 떠나실 건가요?')
        if (answer === false){
            return false // 다른 데로 안가고, 그 자리에 남아있음
        }
    })
</script>

<style scoped>

</style>