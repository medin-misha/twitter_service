<script setup>
import MainCommentForm from './subcomponents/MainCommentForm.vue';
import MainHeader from './subcomponents/MainHeader.vue';
import TweetsComonent from './subcomponents/TweetsComonent.vue';
</script>

<template>
    <div class="main">
        <MainHeader/>
        <MainCommentForm/>
        <TweetsComonent/>
    </div>    
</template>

<style scoped>
.main {
    border: 1px solid #36434d;
}
</style>