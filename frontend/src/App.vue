<script setup>
import Main from "./components/Main.vue"
import Menu from "./components/Menu.vue";
</script>
<template>
  <div class="container flex">
    <Menu/>
    <Main/>
  </div>
</template>

<style scoped>
  .container {
    width: 1200px;
    height: 1000px;
    background: none;
    border: 1px solid #36434d;
    flex-direction: row;
    justify-content:flex-end;
    margin: auto;
  }
</style>
