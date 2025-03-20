<script setup>
import { useTweetFormComponentStore } from "../componentStores/tweetFormComponentStroe";

const tweetStore = useTweetFormComponentStore()

</script>

<template>
    <section class="create-comment-section">
        <form class="flex create-comment-form">
            <div class="flex create-comment-fields">
                <textarea placeholder="Ну шо ты?" name="create-comment-textarea" class="create-comment-textarea"
                    v-model="tweetStore.tweet_data" cols="50" rows="5"></textarea>
                <label for="input-image">
                    <img class="user-input-image" v-if="tweetStore.file" :src="tweetStore.fileUrl" alt="you img">
                    <svg v-if="!tweetStore.file" class="input-file-svg" xmlns="http://www.w3.org/2000/svg" height="24px"
                        viewBox="0 -960 960 960" width="24px" fill="#36434d">
                        <path
                            d="M200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h560q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H200Zm0-80h560v-560H200v560Zm40-80h480L570-480 450-320l-90-120-120 160Zm-40 80v-560 560Z" />
                    </svg>
                </label>
                <input type="file" id="input-image" class="input-image" @change="tweetStore.saveFile">
            </div>
            <button class="create-comment-button" type="button" @click="tweetStore.createTweet()">отправить</button>
        </form>
    </section>
</template>

<style scoped>
.create-comment-section {
    padding-top: .3em;
}

.create-comment-textarea {
    all: unset;
}

.create-comment-textarea {
    border: none;
    background-color: #15202b;
    padding: 10px;
    max-width: 100%;
    line-height: 1.5;
    border-radius: 5px;
    border: 0;
    background: #15202b;
}

.create-comment-form {
    flex-direction: column;

}

.create-comment-fields {
    justify-content: space-around;
    align-content: center;
}

.create-comment-button {
    border-radius: 0;
    border-top: 2px solid #36434d;
}

.input-image {
    display: none;
}

.input-file-svg {
    transition: .2s;
}

.input-file-svg:hover {
    transition: .1s;
    transform: scaleX(1.2) scaleY(1.2);
}

.user-input-image {
    width: 200px;
    border-radius: 5px;
}
</style>