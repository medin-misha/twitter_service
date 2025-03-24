<script setup>
import { ref, watch } from "vue";
import { useAPIStore } from "@/stores/useAPIStore";
import { useLoginStore } from "@/stores/useLoginStore";
import { storeToRefs } from "pinia";

const apiStore = useAPIStore()
const loginStore = storeToRefs(useLoginStore())
const props = defineProps({
    id: Number,
    name: String,
    text: String,
    attachements: Array,
    autor_id: Number,
})
const removeComponent = ref(false)
const noLikeColor = ref("#36434d")
const isLikeColor = ref("#dd1818")
const likeColor = ref("#36434d")
const liked = ref(false)


const Liked = async () => {
    if (liked.value) {
        const response = await apiStore.likeDelete(props.id, loginStore.key.value)
        liked.value = false;
        likeColor.value = noLikeColor.value;

    } else {
        const response = await apiStore.like(props.id, loginStore.key.value)
        liked.value = true;
        likeColor.value = isLikeColor.value;
    }
}

const Delete = async () => {
    const response = await apiStore.deleteTweet(props.id, loginStore.key.value)
    if (response.result) {
        removeComponent.value = true
    }
}

watch(() => loginStore.key.value, () => {
    liked.value = loginStore.myLikes.value.includes(props.id) ? true : false
    if (liked.value) likeColor.value = isLikeColor.value;
    console.log()
})
</script>

<template>
    <article class="flex comment" v-if="!removeComponent">
        <div class="flex author-data">
            <h3>{{ name }}</h3>
            <h4>Id: {{ id }}</h4>

        </div>
        <div class="content">
            <p class="text">{{ text }}</p>
            <img class="tweet-img" v-if="attachements.length > 0" :src="apiStore.url + 'api/medias/' + attachements[0]">
        </div>
        <div class="flex actions">
            <svg class="like" xmlns="http://www.w3.org/2000/svg" height="40px" viewBox="0 -960 960 960" width="40px"
                :fill="likeColor" @click="Liked">
                <path
                    d="m480-152.55-34-31.12q-100.8-92.17-166.89-158.71-66.08-66.54-104.98-118-38.9-51.45-54.14-93.32-15.25-41.87-15.25-84.29 0-81.83 55.19-137.02 55.19-55.19 136.62-55.19 54.05 0 101.16 26.93 47.11 26.94 82.29 78.46 38.6-52.68 84.3-79.03 45.69-26.36 99.23-26.36 81.35 0 136.54 55.13 55.19 55.14 55.19 136.88 0 42.6-15.25 84.48-15.24 41.88-54.1 93.26-38.85 51.37-104.99 118.01Q614.79-275.79 514-183.67l-34 31.12Zm0-63.81q97.52-89.28 160.8-152.76 63.27-63.48 100.35-111.03 37.07-47.54 51.65-84.5 14.57-36.97 14.57-73.21 0-62.35-40.96-103.4-40.96-41.06-102.57-41.06-50.18 0-91.75 29.32-41.58 29.32-71.51 85.54h-41.57q-29.91-55.94-71.65-85.4-41.74-29.46-91.1-29.46-61.33 0-102.48 40.95-41.15 40.96-41.15 103.86 0 36.31 14.81 73.31 14.81 36.99 51.62 84.7 36.8 47.71 100.23 111.01Q382.72-305.18 480-216.36Zm0-283.24Z" />
            </svg>
            <svg v-if="props.autor_id == loginStore.id.value" class="delete" xmlns="http://www.w3.org/2000/svg"
                height="40px" viewBox="0 -960 960 960" width="40px" :fill="noLikeColor" @click="Delete">
                <path
                    d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm400-600H280v520h400v-520ZM360-280h80v-360h-80v360Zm160 0h80v-360h-80v360ZM280-720v520-520Z" />
            </svg>
        </div>
    </article>

</template>

<style scoped>
.comment {
    padding: 1em;
    flex-direction: column;
    justify-items: center;
    border: 1px solid #36434d;
}

.actions {
    flex-direction: row;
    justify-content: space-between;
}

.like {
    transition: .2s;
}

.like:hover {
    transition: .2s;
    transform: scaleX(1.1) scaleY(1.1);
}

.like:active {
    transition: .3s;
    transform: scaleX(1.5) scaleY(1.5);
}

.author-data {
    justify-content: space-between;
}

.tweet-img {
    width: 400px;
    border-radius: 5px;
}
</style>