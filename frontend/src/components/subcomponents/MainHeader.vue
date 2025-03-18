<script setup>
import { useLoginStore } from '@/stores/useLoginStore';
const loginStore = useLoginStore()
</script>

<template >
    <header class="flex">
        <h1>Клон Твиттера</h1>
        <h2 class="header-h2">{{ loginStore.key }} <<<</h2>
    </header>
</template>

<style scoped>
    header {
        width: 800px;
        border: 1px solid #36434d;
        padding: .2em .6em;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
    }
    
    
</style>