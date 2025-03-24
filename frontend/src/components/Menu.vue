<script setup>
import LoginComponent from './subcomponents/LoginComponent.vue';
import { useMainComponentStore } from "./componentStores/mainComponentStore.js"
import { storeToRefs } from 'pinia';

const mainStore = useMainComponentStore()

</script>

<template >
    <nav class="flex navbar">
        <li class="navbar-li flex navbar-main" @click="mainStore.hideAndShowTweets(true)"><span class="navbar-li-span">Главная</span></li>
        <li class="navbar-li flex navbar-users" @click="mainStore.hideAndShowTweets(false)"><span class="navbar-li-span">Пользователи</span></li>
        <li class="navbar-li flex navbar-tweets" @click="mainStore.hideAndShowTweets(true)"><span class="navbar-li-span">Твиты</span></li>
        <button class="create-tweet-button">Твитнуть</button>
        <LoginComponent/>
    </nav>
</template>

<style scoped>
    .navbar {
        height: 1000px;
        width: 400px;
        border: 1px solid #36434d;
        flex-direction: column;
        padding: 1em;
        box-sizing: border-box;
    }
    .navbar-li {
        background: black;
        font-size: 30px;
        list-style-type: none;
        justify-items: left;
        margin-bottom: 20px;
        transition: border 0.3s ease;
        background-position-y: 24px;
        border-bottom: #36434d solid 2px;
        cursor: pointer;

    }
    .navbar-main {
        background: url("public/homeIcon.svg") no-repeat;
        background-position-x: right;
        
    }
    .navbar-users {
        background: url("public/profileIcon.svg") no-repeat;
        background-position-x: right;
    
    }
    .navbar-tweets {
        background: url("public/tweetIcon.svg") no-repeat;
        background-position-x: right;
    
    }
    .navbar-li-span {
        display: block;
    }
    .navbar-li:hover {
        border-bottom: #2196f3 2px solid;
    }
</style>