<script setup>
import MainCommentForm from './subcomponents/MainCommentForm.vue';
import MainHeader from './subcomponents/MainHeader.vue';
import TweetsComonent from './subcomponents/TweetsComonent.vue';
import AutorsComponent from './subcomponents/AutorsComponent.vue';
import { storeToRefs } from 'pinia';
import { useMainComponentStore } from './componentStores/mainComponentStore';

const mainStore = storeToRefs(useMainComponentStore())

</script>

<template>
    <div class="main">
        <MainHeader/>
        <MainCommentForm v-if="mainStore.tweetsComponents.value"/>
        <TweetsComonent v-if="mainStore.tweetsComponents.value"/>
        <AutorsComponent v-if="!mainStore.tweetsComponents.value"/>
    </div>    
</template>

<style scoped>
.main {
    border: 1px solid #36434d;
}
</style>