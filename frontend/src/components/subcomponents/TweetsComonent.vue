<script setup>
import TweetComponent from './TweetComponent.vue';
</script>

<template>
    <section class="flex comments">
        <TweetComponent :liked="false" text="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Earum sunt iusto, voluptates dolore ducimus, enim quisquam porro cumque suscipit placeat eveniet optio, voluptatem est doloribus. Fuga provident ipsa assumenda ullam." name="misha"/>
    </section>
</template>

<style scoped>
.comments {
    flex-direction: column;
}
</style>