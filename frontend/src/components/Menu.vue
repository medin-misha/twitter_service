<script setup>
import LoginComponent from './subcomponents/LoginComponent.vue';
</script>

<template >
    <nav class="flex navbar">
        <li class="navbar-li flex navbar-main"><span class="navbar-li-span">Главная</span></li>
        <li class="navbar-li flex navbar-profile"><span class="navbar-li-span">Профиль</span></li>
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

    }
    .navbar-main {
        background: url("public/homeIcon.svg") no-repeat;
        background-position-x: right;
        
    }
    .navbar-profile {
        background: url("public/profileIcon.svg") no-repeat;
        background-position-x: right;
    
    }
    .navbar-li-span {
        display: block;
    }
    .navbar-li:hover {
        border-bottom: #2196f3 2px solid;
    }
</style>