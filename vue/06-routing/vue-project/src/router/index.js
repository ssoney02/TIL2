import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import UserPosts from '@/components/UserPosts.vue'
import UserProfile from '@/components/UserProfile.vue'
import LoginView from '@/views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      // django에서는 <int:user_pk> 같은 식으로 작성했었음
      // 여기는 vue -> vue에서 변수랑 데이터를 묶는 방법???? => 바인딩!!! :id
      path:'/user/:id',
      // name: 'user',
      component: UserView,
      // 중첩된 라우팅 관리를 위해 children 배열 생성
      children : [
        { path: '', name:'user', component: UserProfile }, //user요청이 오면 메인에 바로 userprofile이 보이도록 하고 싶음
        { path: 'profile', name:'user-profile', component: UserProfile },
        { path: 'posts', name:'user-post', component: UserPosts },
      ]
    },
    // {
    //   path:'user/:id/profile',
    //   name: 'profile',
    //   component: UserPosts
    // },
    // {
    //   path: 'user/:id/posts'
    // }
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        console.log(to,from)
        // 이미 로그인 되어 있는 상태면 원래 위치로 돌아가게!
        const isLoggined = true
        if (isLoggined) {
          return false
          return { name: 'home' }
        }
      }
    }
  ],
})

// router.beforeEach((to, from) => {
//   // 로그인 기능이 실제로 있지는 않으니, 일단 전부 false로 막아보자
//   const isLoggined = false
//   // 만약, 어딘가로 이동하려하는데 로그인 되어 있지 않으면 -> 로그인 페이지로 이동시키기
//   // globally  guard -> 무조건 이동하기 전에 가드가 검사함!
//   // 로그인 페이지로 이동시킬 때도 로그인되어있는지 검사하게됨 => 무한루프.. (isLogined==false니까..)
//   // 로그인 페이지로 이동하는 것 빼고, , 검사하도록 해야!! 
//   if (!isLoggined && to.name !== 'login') {
//     // 로그인 페이지로 redirect
//     alert('로그인하세요!')
//     return {name:'login'}

//   }

//   // from에서 to로 이동하려고 할떄
//   // console.log(to, from)
//   // alert('로그인하세요')
// })

export default router
