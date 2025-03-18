<script setup>
import { useLoginStore } from '@/stores/useLoginStore';
import TweetComponent from './TweetComponent.vue';
import { useAPIStore } from '@/stores/useAPIStore';
import { ref, onMounted } from 'vue';

const apiStrore = useAPIStore();
const loginStore = useLoginStore();
const tweets = ref([])
const getTweets = async () => {
    const response = await apiStrore.getTweets(loginStore.key)
    tweets.value = response.tweets
    return response.tweets;
}
onMounted(() => { getTweets() })
</script>

<template>
    <section class="flex comments">
        <TweetComponent v-for="tweet in tweets" :id="tweet.id" :text="tweet.content" :name="tweet.author.name"
            v-bind:key="tweet.id" />
    </section>
</template>

<style scoped>
.comments {
    flex-direction: column;
}
</style>