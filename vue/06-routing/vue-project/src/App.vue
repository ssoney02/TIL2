<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <!-- to 속성에 route에 정의된 name으로 연결 -->
        <RouterLink :to="{name: 'login'}">Login</RouterLink>
        <!-- 로그인 기능을 만들어 냈다고 가정하고.. -->
         <!-- Globally guard -> 모든 페이지에 로그인되어있지 않으면 접근 못하도록 막을 것! -> index.js에 작성 -->
        <!-- <RouterLink to="/">Home</RouterLink> -->
        <RouterLink :to="{name:'home'}">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <!-- 파라미터가 여러 개 일수도 있음 -> 객체 형식으로 넣어줌 -->
        <RouterLink :to="{name: 'user', params: {'id': 1,}  }">User</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
