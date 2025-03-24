<script setup>
defineProps({
    name: Number,
    id: Number,
})
</script>

<template>
    <article class="flex author" v-if="!removeComponent">
        <div class="flex author-data">
            <h3>{{ name }}</h3>
            <h4>Id: {{ id }}</h4>

        </div>
        <div class="flex actions">
            <button class="subcribe">Подписаться</button>
        </div>
    </article>

</template>

<style scoped>
.author {
    padding: 1em;
    flex-direction: column;
    justify-items: center;
    border: 1px solid #36434d;
}

.actions {
    flex-direction: row;
    justify-content: space-between;
}

.author-data {
    justify-content: space-between;
}
.subcribe {

}
</style>