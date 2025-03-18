<script setup>
import { ref } from "vue";
import { useLoginStore } from '@/stores/useLoginStore';
import { useAPIStore } from "@/stores/useAPIStore";
import { storeToRefs } from 'pinia';
import { useLoginComponentStore } from "../componentStores/loginComponentStore";


const refStore = storeToRefs(useLoginStore())
const apiStore = useAPIStore()
const componentStore = useLoginComponentStore()
const key = ref("");


const getMeApiKey = async (key) => {

    const meResponse = await apiStore.me(key);
    if (meResponse != null) {
        const result = meResponse.result;
        if (result == true) {
            const userName = meResponse.user.name;
            refStore.key.value = key;
            refStore.userName = userName
            componentStore.successLogin()
        }
        return null;
    } else {
        componentStore.errorLogin()
    }

}

</script>

<template>
    <section class="login-section flex">
        <p :class="componentStore.class_">{{ componentStore.text }}</p>
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
    color: white;
}

.login-message {
    transition: 5s;
    color: #2196f3;
    align-self: flex-end;
}

.error-login-message {
    transition: .3s;
    color: rgb(255, 71, 71);
    align-self: flex-end;
}

.success-login-message {
    transition: .3s;
    color: rgb(96, 255, 96);
    align-self: flex-end;
}
</style>