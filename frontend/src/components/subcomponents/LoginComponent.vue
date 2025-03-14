<script setup>
import { ref } from "vue";
import { useLoginStore } from '@/stores/useLoginStore';
import { userAPIStore } from '@/stores/useAPIStore';
import { storeToRefs } from 'pinia';

const refStore = storeToRefs(useLoginStore())
const apiStore = userAPIStore()
const key = ref("");
const isLogin = ref(false);


const getMeApiKey = async (key) => {
    const meResponse = await apiStore.me(key);
    const userName = meResponse.user.name;
    const newKey = meResponse.user.key
    const result = meResponse.result;
    if (result == true) {
        isLogin.value = true;
        refStore.key = newKey;
        refStore.userName = userName
    } else { isLogin.value = false }
    
}

</script>

<template>
    <section class="login-section flex">
        <p v-if="isLogin">hello {{ refStore.userName }}</p>
        <input type="text" class="api-key-input" placeholder="api-key" v-model="key">
        <button @click="getMeApiKey(key)" class="login-button">Авторизоваться</button>
    </section>
</template>

<style scoped>
.login-section {
    align-self: center;
    margin-top: auto;
    flex-direction: column;
}

.api-key-input {
    border: 1px #36434d solid;
    background-color: #15202b;
    padding: 10px;
    width: 300px;
    line-height: 1.5;
    border-radius: 5px;
    background: #15202b;
    margin-bottom: 10px;
}
</style>