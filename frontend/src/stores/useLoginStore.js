import { defineStore } from "pinia"


export const useLoginStore = defineStore("userData", {
    state: () => ({ key: "noAuth", userName: null, myLikes: []}),
    getters: {},
    actions: {},
})
