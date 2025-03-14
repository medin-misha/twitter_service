import { defineStore } from "pinia"


export const useLoginStore = defineStore("userData", {
    state: () => ({ key: "misha", userName: "none"}),
    getters: {},
    actions: {},
})
