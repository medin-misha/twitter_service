<script setup>
import MainCommentForm from './subcomponents/MainCommentForm.vue';
import MainHeader from './subcomponents/MainHeader.vue';
</script>

<template>
    <div class="main">
        <MainHeader/>
        <MainCommentForm/>
    </div>    
</template>

<style scoped>
.main {
    border: 1px solid #36434d;
}
</style>